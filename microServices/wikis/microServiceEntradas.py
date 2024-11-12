import json
import os

from dotenv import load_dotenv
import pymongo
from flask import Blueprint

load_dotenv() 
DB_URL = os.getenv("DB_URL") 

#Creamos el Blueprint

wikis_bp = Blueprint('wikis_bp', __name__)

#Configuracion de MongoDB

client = pymongo.MongoClient(DB_URL)
db = client.ejercicioBackend
wikis = db.wikis 

#A PARTIR DE AQUI VAN LAS RUTAS

@wikis_bp.route("/", methods=['GET'])
def get_wikis():
    return 