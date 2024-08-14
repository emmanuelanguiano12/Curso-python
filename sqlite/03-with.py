import sqlite3

with sqlite3.connect("sqlite/app.db") as con: #Cerrar la conexión y hacer commit

    cursor = con.cursor() #Crear las consultas
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER primary key, nombre VARCHAR(50));
        """
    )
