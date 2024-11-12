import os

from dotenv import load_dotenv
from flask import Flask
from wikis import wikis_bp

load_dotenv()

app = Flask(__name__)

#Registramos los servicios como Blueprints

app.register_blueprint(wikis_bp, url_prefix="/wikis")

#Definimos la ruta predeterminada aqui mismo

@app.route("/")
def main_route():
    return f"<a href='http://127.0.0.1:{os.getenv('SERVICE_WIKIS_PORT')}/wikis'>Click aqui para acceder al apartado de wikis</a>"

#Ejecutar la aplicacion de Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("SERVICE_WIKIS_PORT"))