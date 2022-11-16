from pymongo import MongoClient
import json
import certifi

ca = certifi.where()

#####################################
## Cargar Archivo de Configuración ##
#####################################

def loadConfigFile():
    with open('database/config.json') as f:
        data = json.load(f)
    return data

#####################################
##       Función de Conexión       ##
#####################################  

def dbConnection():
    dataConfig = loadConfigFile()
    try:
        # Conexión Atlas
        client = MongoClient(dataConfig['MONGO_URI_SERVER'], tlsCAFile = ca)
        # Conexión Local
        # client = MongoClient(dataConfig['MONGO_URI_LOCAL'], dataConfig['LOCAL_PORT'])
        db = client["Registraduria_G34"]
    except ConnectionError:
        print("-- Error de Conexíon con la base de datos (db) --")
    return db

