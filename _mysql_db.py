import mysql.connector
from flask import request, session, redirect, render_template

def conectarDB(configDB=None):
    mydb = None
    if configDB != None:
        try: mydb = mysql.connector.connect(
            host = configDB.get("host"),
            user = configDB.get("user"),
            password = configDB.get("pass"),
            database = configDB.get("dbname")
        )
        except Exception as e:
            print(f"No se pudo conectar con la base de datos ---> {e}")
    return mydb

def cerrarDB(mydb):
    if mydb != None:
        mydb.close()

def consultarDB(mydb,sQuery="",val=None,title=False,dictionary=False):
    myresult = None
    try:
        if mydb != None:
            mycursor = mydb.cursor()
            if val == None:
                mycursor.execute(sQuery)
            else:
                mycursor.execute(sQuery,val)
            myresult = mycursor.fetchall()
            if title:
                myresult.insert(0,mycursor.column_names)
            if dictionary:
                keys = mycursor.column_names
                myresult = [dict(zip(keys, row)) for row in myresult]
    except Exception as e:
        print(f"No se ha podido hacer la seleccion con esa query ---> {e}")
    return myresult

def ejecutarDB(mydb,sQuery="",val=None):
    res = None
    try:
        mycursor = mydb.cursor()
        if val == None:
            mycursor.execute(sQuery)
        else:
            val = val
            conjunto = mycursor.execute(sQuery,val,multi=True)
            for result in conjunto:
                val = val
                mydb.commit()
        res = mycursor.rowcount
    except Exception as e:
        mydb.rollback()
        print(f"No se ha podido ejecutar la query ---> {e}")
        raise e
    return res

def selectDB(configDB=None,sQuery="",val=None,title=False,dictionary=False):
    resQuery = None
    if configDB != None:
        mydb = conectarDB(configDB)
        resQuery = consultarDB(mydb,sQuery=sQuery, val=val,title=title,dictionary=dictionary)
        cerrarDB(mydb)
    return resQuery

def insertDB(configDB=None,sQuery="",val=None):
    res = None
    if configDB!=None:
        try:
            mydb=conectarDB(configDB)
            res=ejecutarDB(mydb,sQuery=sQuery,val=val)
            cerrarDB(mydb)
        except Exception as e:
            print(f"Error al iniciar insertDB-->{e}")
            raise e
    return res
        
    
BASE = {
    "host":"localhost",
    "user":"root",
    "pass":"",
    "dbname":"shopandplay"
}