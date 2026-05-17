import sqlite3 as lite

con = lite.connect('banco.db')

with con:

    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS formulario(
        matricula INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        idade INTEGER,
        telefone TEXT,
        dataN DATE,
        sexo TEXT
    )
    """)