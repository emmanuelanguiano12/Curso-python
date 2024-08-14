import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Carlos Pedraza"),
        (3, "Lionel Messi"),
        (4, "Cristiano Ronaldo"),
        (5, "Marco Reus"),
    ]
    cursor.executemany(
        "insert into usuarios values(?, ?)",
        usuarios,
    )