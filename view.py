import sqlite3 as lite

#criando conexao
con = lite.connect('dados.db')

#CRUD

#inserir dados
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO estoque (nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query,i)

#atualizar dados
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE estoque SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query,i)

#deletar dados
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM estoque WHERE id=?"
        cur.execute(query,i)

#ver dados
def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM estoque"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados

#ver dados individuais
def ver_item(id):
    ver_dados_individual = []
    with con:
        cur=con.cursor()
        query = "SELECT * FROM estoque WHERE id=?"
        cur.execute(query,id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)