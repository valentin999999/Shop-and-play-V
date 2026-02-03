from flask import request, session,redirect,render_template
from datetime import datetime
from model import *
from werkzeug.utils import secure_filename

#FUNCIONES PARA EL LAYOUT

def obtenerTopicons(param):
    
    param["topicons"]={
            "right":[
                {"href":"/pagoenvio","ida":"pagobox","contenido":"pago","titulo":"Validar pago","idimg":"pago"},
                {"href":"/","ida":"editarbox","contenido":"edit","titulo":"Editar juego","idimg":"editar"},
                {"href":"/crearjuego","ida":"crearjuegobox","contenido":"plus","titulo":"Añadir juego","idimg":"crearjuego"},
                {"href":"/carrito","ida":"carritobox","contenido":"cart","titulo":"Carrito de compras","idimg":"carrito"},
                {"href":"/pedidos","ida":"historialbox","contenido":"hist","titulo":"Historial de pedidos","idimg":"historial"},
                {"href":"#","ida":"usuariobox","contenido":"user","titulo":"Mi perfil","idimg":"usuario"},
                {"id":"iniciosesion","titulo":"Iniciar Sesión"},
                {"id":"registro","titulo":"Crear cuenta"}
            ],
            "cambio":[
                {"id":"actualizar","texto":"Cambiar datos"},
                {"id":"cerrarsesion","texto":"Cerrar Sesión"}
            ]
    }
    
def obtenerFooter(param):
    param["footer"]='''© SHOP & PLAY S.A. Todos los derechos reservados. Todas las marcas comerciales son propiedad de sus respectivos dueños en Argentina y otros países.
                        Contactanos
                        Shop&Play@gmail.com
                        Av. Rivadavia 27301'''   

def obtenerIdLista():
    if session.get("idlist")==None:
        session["idlist"]=[]

def obtenerLayout(param):
    obtenerTopicons(param)
    obtenerFooter(param)
    obtenerIdLista()
    obtenerListaTitulosJuegos(param)
    obtenerTags(param)

def layoutPagina(param):
    obtenerLayout(param)
    return render_template("layout.html",param=param)

#FUNCIONES PARA LA PAGINA CATÁLOGO

def catalogoPagina(param,msj):
    print(session)
    obtenerLayout(param)
    obtenerListaJuegos(param,msj)
    return render_template("catalogo.html",param=param)

#FUNCIONES PARA LAS PAGINAS DE JUEGOS     
   
def obtenerJuegoElegido(param,name,msj=""):
    obtenerLayout(param)
    obtenerJuegos(param,msj)
    obtenerComprasUsuario(param)
    for juego in param["juegos"]:
        if name.lower()==juego[1].lower():
            param["juegoElegido"]=juego
    obtenerReseñas(param)

def juegoPagina(param,name,msj=""):
    obtenerJuegoElegido(param,name,msj)
    obtenerTagsJuego(param,name)
    return render_template("juego.html",param=param)

def validarEliminarCalificacion(param):
    print(11111)
    miReq = {}
    getRequest(miReq)
    msj = eliminarCalificacion(miReq)
    if not msj:
        param["msj"]="Reseña eliminada"
    else:
        param["msj"]=msj
    obtenerReseñas(param)
    return render_template("reseñas.html",param=param)

#FUNCIONES PARA LA PAGINA DE CARRITO

def carritoPagina(param):
    obtenerLayout(param)
    obtenerJuegosEnCarrito(param)
    obtenerTotal(param)
    return render_template("carrito.html",param=param)

#FUNCIONES PARA AÑADIR UN JUEGO AL CARRITO

def juegoCarrito(param):
    miReq={}
    try:
        getRequest(miReq)
        insertarCompra(miReq)
        quitarStock(miReq)
        res = ""
    except Exception as e:
        print(f"Error al añadir juego al carrito ---> {e}")
        res = "Error al añadir juego al carrito"
    return res

def validarCompra(param):
    msj = juegoCarrito(param)
    if not msj:
        msj = "Juego añadido al carrito"
        res = catalogoPagina(param,msj)
    else:
        res = catalogoPagina(param,msj)
    return res

#FUNCIONES PARA ABONAR JUEGOS

def abonarPagina(param):
    obtenerLayout(param)
    obtenerPago()
    return redirect("/pagoenvio")
    
#FUNCIONES PARA LA PAGINA DE PAGO/ENVIO

def obtenerPagoenvio(param,msj=""):
    param["pagoenvio"]={
        "errores":[
            {"id":"localidad","msj":"La localidad no debe llevar caracteres especiales ni números"},
            {"id":"domicilio","msj":"El domicilio no debe llevar caracteres especiales"},
            {"id":"piso","msj":"El piso no debe llevar caracteres especiales"},
            {"id":"errorgeneral","msj":msj}
        ],
        "titulos":[
            "pickup","delivery"
        ],
        "adi":[
            {"id":"adicuenta","texto":"Cuenta bancaria : 29847411"},
            {"id":"adiformato","texto":"Formatos de imagen permitidos: jpg, jpeg, png, svg, pdf, tiff"}
        ],
        "datotitulo":[
            {"id":"titulofoto","texto":"Foto del comprobante"},
            {"id":"tituloloc","texto":"Localidad"},
            {"id":"titulodom","texto":"Domicilio"},
            {"id":"titulodep","texto":"¿Vive en un departamento?"},
            {"id":"titulopiso","texto":"Piso"}
        ],
        "input":[
            {
                "type":"file",
                "id":"archivo",
                "placeholder":"",
            },
            {   
                "type":"button",
                "id":"confirmar",
                "value":"Confirmar",
                "placeholder":"",
             },
            {   
                "type":"text",
                "id":"datoloc",
                "placeholder":"Introduzca su localidad",
             },
            {   
                "type":"text",
                "id":"datodom",
                "placeholder":"Introduzca su domicilio",
             },
            {   
                "type":"text",
                "id":"datopiso",
                "placeholder":"Introduzca su piso y número de departamento",
             },
        ],
        "dilema":[
            {"id":"si","texto":"Sí"},
            {"id":"no","texto":"No"}
        ]   
    }

def pagoEnvioPagina(param):
    obtenerLayout(param)
    obtenerPagoenvio(param)
    return render_template("pagoenvio.html",param=param)

#FUNCIONES PARA VALIDAR PAGO

def pago(param):
    miReq = {}
    try:
        obtenerLayout(param)
        obtenerPagoenvio(param)
        getRequest(miReq)
        upload_file(miReq)
        idcompra = selectDB(BASE,
                            """SELECT id FROM compra_detalle WHERE id_usuario = %s ORDER BY id DESC LIMIT 1;""",
                            [session.get("id")]
                            )[0][0]
        selectDB(BASE,"SELECT contenido, total, fecha FROM compra_detalle WHERE id=%s;",[idcompra])
        if not miReq.get("datoloc"):
            miReq["datoloc"]="-"
        if not miReq.get("datodom"):
            miReq["datodom"]="-"
        if not miReq.get("datopiso"):
            miReq["datopiso"]="-"
        print(77777)
        insertDB(BASE,
                 "INSERT INTO pago VALUES ('',%s,%s,%s,%s,%s);",
                 (idcompra,miReq["archivo"].get("file_name_new"),miReq["datoloc"],miReq["datodom"],miReq["datopiso"])
                )
        session["pagopendiente"]=False
        session["idlist"].remove(session["id"])
        param["pagoenvio"]["errores"][3]["msj"]=""
    except Exception as e:
        print(f"No se ha podido concretar el pago ---> {e}")
        param["pagoenvio"]["errores"][3]["msj"]="Error al validar el pago"
        traceback.print_exc()
    return render_template("errorpago.html",param=param)


#FUNCIONES PARA LA PAGINA DE PEDIDOS

def pedidosPagina(param):
    obtenerLayout(param)
    obtenerListaPedidos(param)
    return render_template("pedidos.html",param=param)

#FUNCIONES PARA LA PAGINA DE REGISTRO

def obtenerRegistro(param,msj=""):
    param["registro"] = {
        "errores":[
            {"id":"errorgeneral","texto":msj},
            {"id":"erroruser","texto":"El nombre de usuario debe tener entre 3 y 20 caracteres"},
            {"id":"errormail","texto":"El mail debe tener entre 9 y 40 caracteres, debe tener un solo '@', debe tener texto antes de '@' y debe tener una terminación válida. Ej: @gmail.com, @aol.com, @hotmail.com"},
            {"id":"errorpass","texto":"La contraseña debe tener al menos una 8 caracteres y al menos una letra minúscula, una mayúscula, un número y un caracter especial y no debe tener espacios"},
            {"id":"errorpassdos","texto":"Las contraseñas deben coincidir"}
        ],
        "titulos":[
            {"id":"usertitulo","texto":"Nombre de Usuario"},
            {"id":"mailtitulo","texto":"Correo Electrónico"},
            {"id":"passtitulo","texto":"Contraseña"},
            {"id":"passdostitulo","texto":"Repita contraseña"}
        ],
        "inputs":[
            {"type":"text","id":"userinput","placeholder":"Introduzca su nombre de usuario","minlength":"3","value":""},
            {"type":"email","id":"mailinput","placeholder":"Introduzca su correo electrónico","minlength":"8","value":""},
            {"type":"password","id":"passinput","placeholder":"Introduzca su contraseña","minlength":"8","value":""},
            {"type":"password","id":"passinputdos","placeholder":"Repita su contraseña","minlegnth":"0","value":""},
            {"type":"button","id":"crear","placeholder":"null","value":"Crear cuenta","minlegnth":"null"}
        ]
        
    }

def registroPagina(param,msj=""):
    obtenerLayout(param)
    obtenerRegistro(param)
    return render_template("registro.html",param=param)

#FUNCIONES PARA REGISTRAR

def validarUsuario():
    miReq = {}
    try:
        getRequest(miReq)
        res = crearUsuario(miReq.get("userinput"),miReq.get("mailinput"),miReq.get("passinput"))
    except Exception as e:
        print(f"Usuario no ha podido ser evaluado para creacion --> {e}")
        res = "Ha ocurrido un error inesperado al crear la cuenta"
    return res

def ingresoRegistroValido(param):
    obtenerRegistro(param)
    msj = validarUsuario()
    if (not msj):
        param["registro"]["errores"][0]["texto"]="Cuenta creada correctamente"
        res = render_template("errorregistro.html",param=param)
    else:
        param["registro"]["errores"][0]["texto"]=msj
        res = render_template("errorregistro.html",param=param)
    return res

#FUNCIONES PARA LA PAGINA DE INICIAR SESION

def inicioSesionPagina(param):
    obtenerLayout(param)
    obtenerIniciosesion(param)
    return render_template("iniciosesion.html",param=param)

def obtenerIniciosesion(param):
    param["iniciosesion"]={
        "titulos":[
            {"id":"usertitulo","texto":"Nombre de Usuario"},
            {"id":"passtitulo","texto":"Contraseña"}
        ],
        "inputs":[
            {"type":"text","id":"userinput","placeholder":"Introduzca su nombre de usuario","value":""},
            {"type":"password","id":"passinput","placeholder":"Introduzca su contraseña","value":""},
            {"type":"button","id":"login","placeholder":"null","value":"Iniciar Sesión"}
        ]
    }

#FUNCIONES PARA MANEJO DE SESION

def crearSesion(request):
    sesionValida=False
    miReq = {}
    try:
        getRequest(miReq)
        dicUsuario = {}
        if obtenerUsuarioXNombre(dicUsuario, miReq.get("userinput"), miReq.get("passinput")):
            cargarSesion(dicUsuario)
            sesionValida = True
    except Exception as e:
        print(f"No se ha podido crear la sesion ---> {e}")
    return sesionValida

def cargarSesion(dicUsuario):
    print(session.get("id"))
    print(dicUsuario.get("id"))
    print(session.get("pagopendiente"))
    print(session.get("idlist"))
    if dicUsuario.get("id") in session["idlist"]:
        session["pagopendiente"] = True
    else:
        session["pagopendiente"]=False
    session["id"] = dicUsuario["id"]
    session["email"] = dicUsuario["email"]
    session["nombre"] = dicUsuario["nombre"]
    session["password"] = dicUsuario["password"]
    session["rol"] = dicUsuario["rol"]
    session["idcompra"] = ""
    
def ingresoUsuarioValido(param,request):
    obtenerIniciosesion(param)
    if crearSesion(request):
        param["msj"]=""
        res = render_template("errorsesion.html",param=param)
    else:
        param["msj"] = "Nombre de usuario y/o contraseña incorrectos"
        res = render_template("errorsesion.html",param=param) 
    return res

def haySesion():
    return session.get("nombre")!=None

def cerrarSesion():
    try:
        print(session)
        del session["email"]
        del session["nombre"]
        del session["password"]
        del session["rol"]
        if session["pagopendiente"] and session["id"] not in session["idlist"]:
            session["idlist"].append(session["id"])
        del session["pagopendiente"]
        del session["id"]
        print(session)
    except Exception as e:
        print(f"No se ha podido cerrar la sesion ---> {e}")

#FUNCIONES PARA LA PAGINA DE ACTUALIZACION DE DATOS

def obtenerActualizar(param,msj=""):
    param["actualizar"] = {
        "errores":[
            {"id":"errorgeneral","texto":msj},
            {"id":"erroruser","texto":"El nombre de usuario debe tener entre 3 y 20 caracteres"},
            {"id":"errormail","texto":"El mail debe tener entre 9 y 40 caracteres, debe tener un solo '@', debe tener texto antes de '@' y debe tener una terminación válida. Ej: @gmail.com, @aol.com, @hotmail.com"},
            {"id":"errorpass","texto":"La contraseña debe tener al menos una 8 caracteres y al menos una letra minúscula, una mayúscula, un número y un caracter especial y no debe tener espacios"},
            {"id":"errorpassdos","texto":"Las contraseñas deben coincidir"}
        ],
        "titulos":[
            {"id":"usertitulo","texto":"Nombre de Usuario"},
            {"id":"mailtitulo","texto":"Correo Electrónico"},
            {"id":"passtitulo","texto":"Contraseña"},
            {"id":"passdostitulo","texto":"Repita contraseña"}
        ],
        "inputs":[
            {"type":"text","id":"userinput","placeholder":"Introduzca su nombre de usuario","minlength":"3"},
            {"type":"email","id":"mailinput","placeholder":"Introduzca su correo electrónico","minlength":"8"},
            {"type":"password","id":"passinput","placeholder":"Introduzca su contraseña","minlength":"8"},
            {"type":"password","id":"passinputdos","placeholder":"Repita su contraseña","minlegnth":"0"},
            {"type":"button","id":"crear","placeholder":"null","minlegnth":"null"}
        ]
    }

def actualizacionPagina(param):
    obtenerLayout(param)
    obtenerUsuarioDic(param)
    obtenerActualizar(param)
    return render_template("actualizar.html",param=param)

#FUNCIONES PARA ACTUALIZAR DATOS

def obtenerUsuarioDic(param):
    datos = selectDB(BASE,"SELECT nombre_usuario, email, password FROM usuario WHERE id=%s",[session.get("id")])
    if datos:
        param["datos"]=datos[0]

def validarActualizacion(param):
    obtenerUsuarioDic(param)
    param["msj"]=""
    obtenerActualizar(param)
    msj = validarActualizarPagina(param)
    if not msj:
        param["msj"] = "Datos actualizados correctamente"
    else:
        param["actualizar"]["errores"][0]["texto"] = msj
    return render_template("erroractualizar.html",param=param)

#FUNCIONES PARA LA PAGINA DE CREACION DE JUEGOS

def obtenerCrearJuego(param,msj=""):
    param["crearJuego"]={
        "errores":[
            {"id":"nombre","texto":"Introduzca un nombre para el juego"},
            {"id":"desc","texto":"Introduzca una descripción para el juego"},
            {"id":"portada","texto":"Escoja una portada para el juego"},
            {"id":"imagenprincipal","texto":"Escoja una imagen principal para el juego"}
        ],
        "input":[
            {"type":"text","id":"nombre","placeholder":"el nombre","maxlength":"40","label":"Nombre"},
            {"type":"range","id":"precio","placeholder":" ","label":"Precio","min":"1.00","max":"20.00","step":"0.05","value":"1.00","medida":"$"},
            {"type":"text","id":"desc","placeholder":"una breve descripción","maxlength":"500","label":"Descripción"},
            {"type":"range","id":"stock","placeholder":" ","label":"Stock","min":"1","max":"50","step":"1","value":"1","medida":"Unidad/es"},
            {"type":"file","id":"portada","placeholder":" ","label":"Portada"},
            {"type":"file","id":"imagenprincipal","placeholder":" ","label":"Imagen principal"}
        ],
        "label":[
            {"titulo":"Nombre"},
            {"titulo":"Precio"},
            {"titulo":"Descripción"},
            {"titulo":"Stock"},
            {"titulo":"Portada"},
            {"titulo":"Imagen principal"},
        ]
        
    }
    param["msj"]=msj

def crearJuegoPagina(param,msj=""):
    obtenerLayout(param)
    obtenerCrearJuego(param,msj)
    return render_template("crearjuego.html",param=param)

def validacionJuego(param):
    obtenerLayout(param)
    obtenerCrearJuego(param)
    obtenerTags(param)
    msj = cargarJuego(param)
    if not msj:
        param["msj"]= "Juego creado correctamente"
    else:
        param[msj]=msj
    return render_template("errorcrear.html",param=param)

#FUNCIONES PARA LA PAGINA DE RESULTADOS

def obtenerBusqueda(param):
    getRequest(param)
    return param["searchbar"]

def obtenerJuegosBuscados(param):
    param["juegosBuscados"]=[]
    busq = obtenerBusqueda(param).upper()
    if busq[0]!="#":
        obtenerListaJuegos(param,"")
        for juego in param["listaJuegos"]:
            if busq in juego[0].upper():
                param["juegosBuscados"].append(juego)
        if len(param["juegosBuscados"])==0:
            param["vacio"]="No se ha encontrado ningún resultado para la búsqueda '"
        else:
            param["vacio"]=""
        print(param["juegosBuscados"])
    else:
        obtenerTags(param)
        param["juegosBuscados"]=[]
        listaIdJuegos = obtenerJuegoConTag(busq[1:])
        for id in listaIdJuegos:
            juego = selectDB(BASE,"SELECT titulo, portada, FORMAT(precio, 2), stock FROM juego WHERE id=%s",[id])[0]
            param["juegosBuscados"].append(juego)
        print(param["juegosBuscados"])
            
            

def resultadosPagina(param):
    obtenerLayout(param)
    obtenerJuegosBuscados(param)
    return render_template("resultados.html",param=param)

#FUNCIONES PARA LA PAGINA DE EDICION DE JUEGOS

def obtenerEditarJuego(param,msj=""):
    param["editarjuego"]={
        "input":[
            {"type":"text","id":"nombre","placeholder":"el nombre","maxlength":"40","label":"Nombre"},
            {"type":"range","id":"precio","placeholder":" ","label":"Precio","min":"1.00","max":"20.00","step":"0.05","value":"1.00","medida":"$"},
            {"type":"text","id":"desc","placeholder":"una breve descripción","maxlength":"500","label":"Descripción"},
            {"type":"range","id":"stock","placeholder":" ","label":"Stock","min":"1","max":"50","step":"1","value":"1","medida":"Unidad/es"},
            {"type":"file","id":"portada","placeholder":" ","label":"Portada"},
            {"type":"file","id":"imagenprincipal","placeholder":" ","label":"Imagen principal"}
        ],
        "label":[
            {"titulo":"Nombre"},
            {"titulo":"Precio"},
            {"titulo":"Descripción"},
            {"titulo":"Stock"},
            {"titulo":"Portada"},
            {"titulo":"Imagen principal"},
        ]
        
    }
    param["msj"]=msj

def editarJuegoPagina(param,name):
    obtenerLayout(param)
    obtenerEditarJuego(param)
    param["juegoeditado"]=[]
    datos = selectDB(BASE,
                     "SELECT titulo, precio, descripcion, stock, portada, imagen_principal, id FROM juego WHERE titulo = %s",
                     [name])[0]
    for dato in datos:
        param["juegoeditado"].append(dato)
    i = 0
    while i < len(param["juegoeditado"]) and i < len(param["editarjuego"]["input"]):
        param["editarjuego"]["input"][i]["value"]=param["juegoeditado"][i]
        i+=1
    return render_template("editarjuego.html",param=param)

def edicionValida(param,name):
    obtenerLayout(param)
    obtenerEditarJuego(param)
    param["juegoeditado"]=[]
    datos = selectDB(BASE,
                     "SELECT titulo, precio, descripcion, stock, portada, imagen_principal, id FROM juego WHERE titulo = %s",
                     [name])[0]
    for dato in datos:
        param["juegoeditado"].append(dato)
    i = 0
    while i < len(param["juegoeditado"]) and i < len(param["editarjuego"]["input"]):
        param["editarjuego"]["input"][i]["value"]=param["juegoeditado"][i]
        i+=1
    msj = editarjuego(param)
    if not msj:
        param["msj"]="Datos del juego editados correctamente"
    else:
        param["msj"]=msj
    return render_template("erroredicion.html",param=param)

def editarjuego(param):
    try:
        miReq = {}
        getRequest(miReq)
        upload_file(miReq)
        insertDB(BASE,"UPDATE juego SET titulo=%s, precio=%s, stock=%s, descripcion=%s, portada=%s, imagen_principal=%s WHERE id=%s;",
                 (miReq.get("juegonombre"),
                  miReq.get("juegoprecio"),
                  miReq.get("juegostock"),
                  miReq.get("juegodesc"),
                  miReq.get("juegoportada").get("file_name_new"),
                  miReq.get("juegoimagenprincipal").get("file_name_new"),
                  miReq.get("idjuego"))
                )
        res = ""
    except Exception as e:
        print(f"No se ha podido validar la edicion --> {e}")
        res = "Nombre de juego no disponible"
    return res

#######

def obtenerTagsJuego(param,name):
    tags = selectDB(BASE,"SELECT tags FROM juego WHERE titulo=%s",[name])[0][0].split(",")
    param["tagsjuego"]=tags

def obtenerTags(param):
    tags = selectDB(BASE,"SELECT tags FROM juego")
    tagLst = []
    for set in tags:
        tagset = set[0].split(",")
        for tag in tagset:
            if tag not in tagLst and tag:
                tagLst.append(tag)
    param["tags"]=tagLst
    

def obtenerJuegoConTag(miTag):
    tags = selectDB(BASE,"SELECT tags, id FROM juego")
    idLst = []
    for set in tags:
        tagset = set[0].split(",")
        for tag in tagset:
            if miTag in tag.upper() and set[1] not in idLst:
                idLst.append(set[1])     
    return idLst
    
    
