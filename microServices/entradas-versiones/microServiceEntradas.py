import json
import os

from dotenv import load_dotenv
import pymongo
from flask import Blueprint

load_dotenv() 
DB_URL = os.getenv("DB_URL") 

#Creamos el Blueprint

entradas_bp = Blueprint('entradas_bp', __name__)

#Configuracion de MongoDB

client = pymongo.MongoClient(DB_URL)
db = client.ejercicioBackend
entradas = db.entradas 

#A PARTIR DE AQUI VAN LAS RUTAS

@entradas_bp.route("/", methods=['GET'])
def get_entradas():
    return 