import sqlite3

def conectar():
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            dni INTEGER NOT NULL,
            cont TEXT NOT NULL
        )
        ''')
    conn.commit()
    conn.close()

def insertar_usuario(usuario, dni, cont):
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuario (usuario, dni, cont)
        VALUES (?, ?, ?)
    ''', (usuario, dni, cont))
    conn.commit()
    conn.close()

def ver_usuarios():
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT usuario, dni, cont FROM usuario")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios
