from _mysql_db import *
import traceback
from mysql.connector import errorcode
import os
from appConfig import config
from uuid import uuid4



#FUNCIONES PARA LA PAGINA DE CATALOGO

def obtenerListaJuegos(param,msj):
    param["msj"]=msj
    param["listaJuegos"]=[]
    datos=selectDB(BASE, "SELECT titulo, portada, FORMAT(precio, 2), stock FROM juego")
    for juego in datos:
        param["listaJuegos"].append(juego)

#FUNCIONES PARA LA PAGINA DE LAYOUT

def obtenerListaTitulosJuegos(param):
    param["listaTitulosJuegos"]=[]
    datos = selectDB(BASE, "SELECT titulo, stock FROM juego;",title=False)
    for nombre in datos:
        if nombre[1] != 0:
            param["listaTitulosJuegos"].append(nombre[0])
            
#FUNCIONES PARA LAS PAGINAS DE LOS JUEGOS

def obtenerJuegos(param,msj):
    param["juegos"]=[]
    datos = selectDB(BASE,"SELECT * FROM juego")
    for juego in datos:
        param["juegos"].append(juego)
    param["msj"]=msj
        
def obtenerComprasUsuario(param):
    param["compras"]=[]
    datos = selectDB(BASE,"SELECT id_juego FROM compra WHERE id_usuario=%s AND estado='en carrito'",[session.get("id")])
    for compra in datos:
        param["compras"].append(compra[0])
        
def obtenerReseñas(param):
    try:
        param["reseñas"]=[]
        datos = selectDB(BASE,"""SELECT usuario.nombre_usuario, estrella.cantidad, estrella.id FROM estrella 
                        INNER JOIN usuario ON usuario.id = estrella.id_usuario 
                        INNER JOIN juego ON juego.id = estrella.id_juego
                        WHERE juego.id = %s;""",[param["juegoElegido"][0]])
        for reseña in datos:
            param["reseñas"].append(reseña)
    except Exception as e:
        print(f"No se pudo obtener las reseñas --> {e}")

def generarReseña(param):
    print(7777)
    try:
        miReq={}
        getRequest(miReq)
        print(miReq)
        insertDB(BASE,
                "INSERT estrella VALUES ('',%s,%s,%s)",
                (session.get("id"),miReq["idjuego"][0],miReq["tunumero"])
                )
        obtenerReseñas(param)
        param["msj"]="Reseña enviada"
    except Exception as e:
        print(f"Error al generar reseña ---> {e}")
        param["msj"]="Error al enviar reseña"
    return render_template("reseñas.html",param=param)

def eliminarCalificacion(miReq):
    try:
        insertDB(BASE,"DELETE FROM estrella WHERE id=%s",[miReq["reseñaId"]])
        res = ""
    except Exception as e:
        print(f"Error al eliminar reseña ---> {e}")
        res = "Error al eliminar reseña"
    return res

#FUNCIONES PARA ACTUALIZAR DATOS

def validarActualizarPagina(param):
    miReq = {}
    try:
        getRequest(miReq)
        insertDB(BASE,
                 "UPDATE usuario SET nombre_usuario = %s, email = %s, password = %s WHERE id=%s",
                 (miReq.get("userinput"),miReq.get("mailinput"),miReq.get("passinput"),session.get("id"))
                )
        session["nombre"]=miReq.get("userinput")
        session["email"]=miReq.get("mailinput")
        session["password"]=miReq.get("passinput")
        msj = ""
    except mysql.connector.Error as error:
        print(f"No se ha podido validar la actualizacion de datos ---> {error}")
        error = str(error)
        if error.endswith("'un_nombre_usuario'"):
            msj = "Nombre de usuario no disponible"
        elif error.endswith("'un_email_usuario'"):
            msj = "Correo no disponible"
        else:
            msj = "Ocurrió un error inesperado"
    return msj
        
#FUNCIONES PARA LA PAGINA DE CARRITO 

def obtenerJuegosEnCarrito(param):
    param["carritoJuegos"]=[]
    datos=selectDB(BASE,"""SELECT juego.portada, juego.titulo, juego.precio, compra.cantidad, compra.id, juego.id FROM compra  
                   INNER JOIN juego ON compra.id_juego = juego.id 
                   WHERE compra.estado='en carrito' AND compra.id_usuario=%s;""",[session.get("id")])
    
    for compra in datos:
        param["carritoJuegos"].append(compra)

def obtenerTotal(param):
    total = selectDB(BASE,
                    """SELECT ROUND(SUM(compra.cantidad*juego.precio),2) FROM compra
                    INNER JOIN juego ON juego.id=compra.id_juego
                    WHERE compra.id_usuario = %s AND compra.estado = "en carrito";""",
                    [session.get("id")])
    param["montoinicial"]=total[0][0]
    print(param["montoinicial"])

#FUNCIONES PARA AÑADIR UN JUEGO AL CARRITO

def insertarCompra(miReq):
    usuario = int(session["id"])
    juego = int(miReq["idjuego"])
    cantidad = int(miReq["unidadinput"])
    estado = 'en carrito'
    try:
        query = "INSERT compra VALUES ('',%s,%s,%s,%s);"
        insertDB(BASE,query,(usuario,juego,cantidad,estado))
    except Exception as e:
        print(f"No se ha podido insertar la compra -->{e}")

def quitarStock(req):
    stock = selectDB(BASE,"SELECT stock FROM juego WHERE id = %s",[req["idjuego"]])[0][0]
    insertDB(BASE,"UPDATE juego SET stock = %s WHERE id = %s",(stock - int(req["unidadinput"]),req["idjuego"]))

#FUNCIONES PARA QUITAR UN JUEGO DEL CARRITO

def quitarJuegoCarrito(param):
    miReq = {}
    getRequest(miReq)
    print(miReq)
    cantidad = list(miReq.keys())[1]
    idjuego = list(miReq.keys())[2]
    idcompra = list(miReq.keys())[3]
    insertDB(BASE,"DELETE FROM compra WHERE id=%s;",[miReq[idcompra][0]])
    stock = selectDB(BASE,"SELECT stock FROM juego WHERE id=%s;",[int(miReq[idjuego])])[0][0]
    insertDB(BASE,"UPDATE juego SET stock=%s WHERE id=%s;",(stock+int(miReq[cantidad]),miReq[idjuego]))
    obtenerJuegosEnCarrito(param)
    return render_template("listajuegos.html",param=param)

#FUNCIONES PARA ABONAR JUEGOS

def obtenerPago():
    session["pagopendiente"]=True
    session["idlist"].append(session["id"])
    miReq = {}
    try:
        print(session)
        getRequest(miReq)
        compraCantidad = len(selectDB(BASE,"SELECT * FROM compra_detalle"))+1
        insertDB(BASE,
                 "INSERT compra_detalle VALUES (%s,%s,%s,%s,%s);",
                 (compraCantidad,int(session["id"]),miReq["inputproducto"],float(miReq["inputvalor"]),miReq["inputfecha"])
                )
        listaCantidadCompras = []
        cadena = miReq["inputproducto"]
        while cadena.find(")") != -1:
            tupla = tuple(cadena[cadena.find("(")+1:cadena.find(")")].split(","))
            cantidad = int(tupla[1])
            listaCantidadCompras.append(cantidad)
            cadena = cadena[cadena.find(")")+1:]
        idJuegos = selectDB(BASE,
                            "SELECT id_juego FROM compra WHERE id_usuario=%s AND estado = 'en carrito';",
                            [session["id"]]
                            )
        listaIdJuegos=[]
        for id in idJuegos:
            listaIdJuegos.append(id[0])
        
        i = 0
        while i<len(listaIdJuegos):
            insertDB(BASE,
                    "UPDATE compra SET cantidad = %s, estado = 'pagado' WHERE id_usuario = %s AND id_juego = %s AND estado = 'en carrito'",
                    (listaCantidadCompras[i],session["id"],listaIdJuegos[i]))     
            i+=1
        listaAdiStock = miReq["inputstock"].split(",")
        j = 0
        while j < len(listaAdiStock):
            listaAdiStock[j] = int(listaAdiStock[j])
            j+=1
        k = 0
        while k < len(listaIdJuegos):
            stockInicial = selectDB(BASE,"SELECT stock FROM juego WHERE id=%s",[listaIdJuegos[k]])[0][0]
            insertDB(BASE,"UPDATE juego SET stock = %s WHERE id=%s",(stockInicial+listaAdiStock[k],listaIdJuegos[k]))
            k+=1
    except Exception as e:
        print(f"No se ha podido obtener el pago ---> {e}")
        traceback.print_exc()

#FUNCIONES PARA VALIDAR PAGO



#FUNCIONES PARA CREAR JUEGOS

def cargarJuego(param):
    try:
        miReq={}
        getRequest(miReq)
        upload_file(miReq)
        param["nuevoJuego"]=miReq
        tagStr = ""
        for key in miReq:
            if "tag" in key:
                tagStr+=miReq[key]+","
        tagStr=tagStr[:len(tagStr)-1]
        insertDB(BASE,
                 "INSERT juego VALUES ('',%s,%s,%s,%s,%s,%s,%s);",
                 (miReq.get("juegonombre"),
                  float(miReq.get("juegoprecio")),
                  int(miReq.get("juegostock")),
                  miReq.get("juegodesc"),
                  miReq.get("juegoportada").get("file_name_new"),
                  miReq.get("juegoimagenprincipal").get("file_name_new"),
                  tagStr
                 )
                )
        res = ""
    except Exception as error:
        print(f"No se ha podido cargar el juego ---> {error}")
        res = "Título del juego no disponible"
    return res

#FUNCIONES PARA CREAR SESION

def getRequest(diResult):
    print(request.files)
    if request.method == "POST":
        for name in request.form.to_dict().keys():
            li = request.form.getlist(name)
            if len(li)>1:
                diResult[name] = li
            elif len(li)==1:
                diResult[name] = li[0]
            else:
                diResult[name] = ""
    elif request.method == "GET":
        for name in request.args.to_dict().keys():
            li=request.args.getlist(name)
            if len(li)>1:
                diResult[name] = li
            elif len(li)==1:
                diResult[name] = li[0]
            else:
                diResult[name] = ""

def obtenerUsuarioXNombre(diResult,nombre,password):
    res=False
    sQuery="""SELECT * FROM usuario WHERE nombre_usuario=%s AND password=%s;"""
    val=(nombre,password)
    fila=selectDB(BASE,sQuery,val)
    print(BASE,sQuery,val)
    if fila!=[]:
        res = True
        diResult["id"]=fila[0][0]
        diResult["nombre"]=fila[0][1]
        diResult["email"]=fila[0][2]
        diResult["password"]=fila[0][3]
        diResult["rol"]=fila[0][4]
    return res

#FUNCIONES PARA MOSTRAR PEDIDOS

def obtenerListaPedidos(param):
    param["pedidos"]=[]
    datos = selectDB(BASE, """SELECT pago.id AS id,
                     usuario.email AS email,
                     compra_detalle.contenido AS contenido,
                     compra_detalle.fecha AS fecha,
                     pago.comprobante AS comprobante,
                     pago.localidad AS localidad,
                     pago.domicilio AS domicilio,
                     pago.piso AS piso,
                     compra_detalle.total AS total
                     FROM pago
                     INNER JOIN compra_detalle ON compra_detalle.id=pago.id_compra_detalle
                     INNER JOIN usuario ON usuario.id = compra_detalle.id_usuario""",
                    title=True)
    for pedidotupla in datos:
        param["pedidos"].append(pedidotupla)

#FUNCIONES PARA CREAR CUENTA

def crearUsuario(username,email,password):
    try:
        insertDB(BASE,"INSERT usuario VALUES ('',%s,%s,%s,'buyer');",(username,email,password))
        res = ""
    except Exception as e:
        print(f"Usuario no creado --> {e}")
        e = str(e)
        if e.endswith("un_nombre_usuario'"):
            res = "Nombre de usuario no disponible"
        elif e.endswith("un_email_usuario'"):
            res = "Correo no disponible"
        else:
            res = "Ha ocurrido un error inesperado al crear la cuenta"
    return res

#FUNCIONES PARA SUBIDA DE ARCHIVOS

def upload_file (diResult) :
    UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif', '.jpeg', '.svg', '.pdf', '.tiff']
    MAX_CONTENT_LENGTH = 1024 * 1024     
    if request.method == 'POST' :         
        for key in request.files.keys():  
            diResult[key]={} 
            diResult[key]['file_error']=False            
            
            f = request.files[key] 
            if f.filename!="":     
                #filename_secure = secure_filename(f.filename)
                file_extension=str(os.path.splitext(f.filename)[1])
                filename_unique = uuid4().__str__() + file_extension
                path_filename=os.path.join( config['upload_folder'] , filename_unique)
                # Validaciones
                if file_extension not in UPLOAD_EXTENSIONS:
                    diResult[key]['file_error']=True
                    diResult[key]['file_msg']='Error: No se admite subir archivos con extension '+file_extension
                if os.path.exists(path_filename):
                    diResult[key]['file_error']=True
                    diResult[key]['file_msg']='Error: el archivo ya existe.'
                    diResult[key]['file_name']=f.filename
                try:
                    if not diResult[key]['file_error']:
                        diResult[key]['file_error']=True
                        diResult[key]['file_msg']='Se ha producido un error.'

                        f.save(path_filename)   
                        diResult[key]['file_error']=False
                        diResult[key]['file_name_new']=filename_unique
                        diResult[key]['file_name']=f.filename
                        diResult[key]['file_msg']='OK. Archivo cargado exitosamente'
 
                except:
                        pass
            else:
                diResult[key]={}


