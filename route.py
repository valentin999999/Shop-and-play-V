from flask import render_template, request
from controller import *
from _mysql_db import *
global param
param = {}

def route(app):
    @app.route("/layout")
    def cargarLayout():
        param={}
        return layoutPagina(param)
    
    @app.route("/")
    @app.route("/catalogo")
    def cargarCatalogo():
        param = {}
        msj = ""
        return catalogoPagina(param,msj)
    
    @app.route("/juego/<name>", methods=["GET","POST"])
    def juego(name):
        param = {}
        print(name)
        obtenerJuegoElegido(param,name)
        return juegoPagina(param,name)
    
    @app.route("/juego/<name>/calificarJuego", methods=["GET","POST"])
    def calificarJuego(name):
        obtenerJuegoElegido(param,name)
        return generarReseña(param)
    
    @app.route("/juego/<name>/eliminarReseña", methods=["GET","POST"])
    def eliminarReseña(name):
        param = {}
        obtenerJuegoElegido(param,name)
        return validarEliminarCalificacion(param)
    
    @app.route("/añadirJuegoCarrito", methods = ["GET","POST"])
    def añadirJuegoCarrito():
        param = {}
        msj = ""
        return validarCompra(param)
    
    @app.route("/carrito", methods=["GET","POST"])
    def cargarCarrito():
        param = {}
        return carritoPagina(param)
    
    @app.route("/eliminarJuegoCarrito", methods= ["GET","POST"])
    def eliminarJuegoCarrito():
        param = {}
        return quitarJuegoCarrito(param)
    
    @app.route("/abonar",methods=["GET","POST"])
    def abonar():
        param = {}
        return abonarPagina(param)
    
    @app.route("/pagoenvio", methods=["GET","POST"])
    def cargarPago():
        param = {}
        return pagoEnvioPagina(param)
    
    @app.route("/validarpago", methods = ["GET","POST"])
    def validarPago():
        param = {}
        return pago(param)
    
    @app.route("/pedidos")
    def cargarPedidos():
        param = {}
        return pedidosPagina(param)
    
    @app.route("/resultados")
    def cargarResultados():
        param = {}
        return resultadosPagina(param)

    @app.route("/registro", methods = ["GET","POST"])
    def cargarRegistro():
        param = {}
        return registroPagina(param)
    
    @app.route("/validarregistro", methods = ["GET","POST"])
    def validarRegistro():
        param = {}
        return ingresoRegistroValido(param)
    
    @app.route("/iniciosesion", methods = ["GET","POST"])
    def cargarInicioSesion():
       param = {}
       return inicioSesionPagina(param)
        
    @app.route("/validarsesion", methods =["GET", "POST"])
    def validarSesion():
        param = {}
        return ingresoUsuarioValido(param,request)
    
    @app.route("/actualizar", methods = ["GET","POST"])
    def cargarActualizacion():
        param={}
        return actualizacionPagina(param)
    
    @app.route("/validaractualizar", methods = ["GET","POST"])
    def validarActualizar():
        param = {}
        return validarActualizacion(param) 
      
    @app.route("/cerrarsesion")
    def finsesion():
        param = {}
        cerrarSesion()
        return catalogoPagina(param,"Sesión cerrada")
    
    @app.route("/crearjuego", methods = ["GET","POST"])
    def crearJuego():
        param={}
        return crearJuegoPagina(param)

    @app.route("/validarjuego", methods = ["GET","POST"])
    def validarjuego():
        param = {}
        return validacionJuego(param)

    @app.route("/juego/<name>/editarjuego", methods = ["GET","POST"])
    def editarjuego(name):
        param = {}
        return editarJuegoPagina(param,name)

    @app.route("/juego/<name>/validaredicion", methods = ["GET","POST"])
    def validaredicion(name):
        param = {}
        return edicionValida(param,name)

#Filtros
    '''
    param["gentle"]=[1,2,3,4,5,6]
    param["dic"]={"Ulises":1,"Adiox":4,"8cho":9}
    param["ulala"]=[2,4]
    param["diablo"]="Has muerto %s, el %s de %s de %s"
    param["inicio"] =[{"name":"tobias","pais":"argelia"},{"name":"alicia","pais":"jamaica"},{"name":"jacob","pais":"brasil"}]
    param["unite"]=["No","Me","pegues","Hijo","de","puta"]
    param["retraso"]="ANDATEATUCUARTO"
    param["elefante"]=[{"music":"Coincidentia Oppositorum","id":3},{"music":"Cradle of History","id":7},{"music":"Tri Repetae","id":1}]
    param["numeritos"]=[1,2,1,2,1,2,21,2,1,2,2,1]
    param["electro1"]=[{"state":"on","cosa":"celu"},{"state":"off","cosa":"compu"},{"state":"on","cosa":"tablet"}]
    param["electro2"]=[{"state":"on","cosa":"celu"},{"state":"off","cosa":"compu"},{"state":"on","cosa":"tablet"}]
    param["nuevo"]=[1,2,4,1,2,1,2,3,41,1,1,5,1]
    param["condi"]=[1,2,3,4,5,6]
    param["uuu"]=["A","B","C","D","E","F"]
    param["pru"]="<h1> aeiou aeiou </h1>"
    param["electro3"]=[{"state":"on","cosa":"celu"},{"state":"off","cosa":"compu"},{"state":"on","cosa":"tablet"}]
    param["discri"]=[1,2,3,4,5,4,32,1,5]
    param["visita"]="Visitame a mi canal: https://youtube.com"
    param["texto"]="No hay nada de calor en tu casa pero si te da un chucho anda a por el hielo de la pieza"
    
    #Pruebas
    def rounda():
        pass
    
    param["test"]=[0,1,2,3,4,5,False,True,True]
    param["otro"]={}
    
    #child
    '''










    