import sqlite3 

conexao = sqlite3.connect("cinema.db")

tabela = """

CREATE TABLE IF NOT EXISTS filmes(
    
  codigo INTEGER PRIMARY KEY AUTOINCREMENT,
  titulo VARCHAR(50),  
  genero VARCHAR(50),
  duracao FLOAT,
  classificacao_indicativa FLOAT
)

"""

consulta = conexao.cursor()

consulta.execute(tabela)



