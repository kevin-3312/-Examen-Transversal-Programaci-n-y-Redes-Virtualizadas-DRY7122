from flask import Flask
import sqlite3
import bcrypt

app = Flask(__name__)

DB = "usuarios.db"

# Crear base de datos
conexion = sqlite3.connect(DB)
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

conexion.commit()

# Integrantes y contraseñas
usuarios = [
    ("Kevin Lipin", "Kevin123"),
    ("Constanza Digmann", "Constanza123"),
    ("Israel Miranda", "Israel123")
]

# Insertar usuarios con contraseña en hash
for nombre, password in usuarios:

    cursor.execute("SELECT * FROM usuarios WHERE nombre=?", (nombre,))

    if cursor.fetchone() is None:

        hash_password = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        ).decode()

        cursor.execute(
            "INSERT INTO usuarios(nombre,password) VALUES(?,?)",
            (nombre, hash_password)
        )

conexion.commit()
conexion.close()


@app.route("/")
def inicio():

    conexion = sqlite3.connect(DB)
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre FROM usuarios")

    datos = cursor.fetchall()

    conexion.close()

    salida = "<h2>Integrantes registrados</h2><ul>"

    for usuario in datos:
        salida += f"<li>{usuario[0]}</li>"

    salida += "</ul>"

    return salida


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5800)
