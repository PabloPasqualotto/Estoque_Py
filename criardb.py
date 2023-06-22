import sqlite3 as lite

con = lite.connect('dados.db')

with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE estoque(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_da_compra DATE, valor_da_compra DECIMAL, serie TEXT, imagem TEXT)")