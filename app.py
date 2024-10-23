import sqlite3
from flask import Flask, render_template, request
import conexion

app = Flask(__name__)


conexion.conectar()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")


@app.route("/datos", methods=["GET", "POST"])
def datos_obtenidos():
    if request.method == "POST":
        usuario = request.form["usuario"]
        dni = request.form["dni"]
        cont = request.form["cont"]

        conexion.insertar_usuario(usuario, dni, cont)

        return render_template("datos.html", usuario=usuario, dni=dni, cont=cont)
    else:
        return "No se encontraron datos"
    
    
@app.route("/usuarios")
def mostrar_usuarios():
    usuarios = conexion.ver_usuarios() 

    return render_template("usuarios.html", usuarios=usuarios)