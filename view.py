import sqlite3 as lite

con = lite.connect('banco.db')


def inserirInfo(i):
    with con:
        cur = con.cursor()
        query = """
        INSERT INTO formulario
        (nome, email, idade, telefone, dataN, sexo)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cur.execute(query, i)


def mostrarInfo():

    lista = []

    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()
        for i in informacao:
            lista.append(i)

    return lista


def atualizarInfo(lista):
    with con:
        cur = con.cursor()
        query = """
        UPDATE formulario
        SET nome = ?, email = ?, idade = ?, telefone = ?, dataN = ?, sexo = ?
        WHERE matricula = ?
        """
        cur.execute(query, lista)


def deletarInfo(matricula):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE matricula = ?"
        cur.execute(query, (matricula,))