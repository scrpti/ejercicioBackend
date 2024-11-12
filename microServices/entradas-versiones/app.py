import os

from dotenv import load_dotenv
from flask import Flask
from entradas import entradas_bp

load_dotenv()

app = Flask(__name__)

#Registramos los servicios como Blueprints

app.register_blueprint(entradas_bp, url_prefix="/entradas")

#Definimos la ruta predeterminada 

@app.route("/")
def main_route():
    return f"<a href='http://127.0.0.1:{os.getenv('SERVICE_ENTRADAS_PORT')}/entradas'>Click aqui para acceder al apartado de entradas</a>"

#Ejecutar la aplicacion de Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("SERVICE_ENTRADAS_PORT"))