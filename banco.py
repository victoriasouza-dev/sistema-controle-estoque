#  Conexão + criação de tabela.

import sqlite3



def conectar_banco():
    conexao = sqlite3.connect("estoque.db")
    return conexao


def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produto(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    )
    """)


    conexao.commit()
    conexao.close()