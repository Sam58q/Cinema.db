import sqlite3
class Filme:
    def conexao(self):
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
        return conexao
    
    def cadastrarFilme(self,titulo,genero,duracao,classificacao_indicativa):
        conexao = self.conexao()
        sql = "INSERT INTO filmes VALUES(?,?,?,?,?)"
        
        campos = (None,titulo,genero,duracao,classificacao_indicativa)
        consulta = conexao.cursor()
        consulta.execute(sql,campos)
        
        conexao.commit()
        print(consulta.rowcount,"linha(s) inseridas(s) com sucesso\n")
        conexao.close()
                   
    def consultarFilmes(self):
        conexao = self.conexao()
        consulta = conexao.cursor()
        sql = "SELECT * FROM filmes"
        consulta.execute(sql)
        resultado = consulta.fetchall()
        
        for item in resultado:
            print(f"codigo: {item[0]}")
            print(f"título: {item[1]}")
            print(f"gênero: {item[2]}")
            print(f"duração:{item[3]}")
            print(f"classificacao_indicativa:{item[4]}")
        conexao.close()
                
    def consultarFilmeindividual(self,codigo):
        conexao = self.conexao()
        consulta = conexao.cursor()
        sql = "SELECT * FROM filmes WHERE codigo = ?"
        campos = (codigo,)
        consulta.execute(sql,campos)
        conexao.commit()
        resultado = consulta
        
        for item in resultado:
            print(f"titulo: {item[0]}")
            print(f"Genero: {item[1]}")
            print(f"duração: {item[2]}")
            print(f"classificacao_indicativa: {item[3]}")
            
        conexao.close()
        
     
    def deletarFilme(self,codigo):
        conexao = self.conexao()
        consulta = conexao.cursor()
        sql = "DELETE FROM filmes WHERE codigo = ?"
        campos = (codigo,)
        consulta.execute(sql,campos)
        conexao.commit()
        if consulta.rowcount > 0:  
         print(consulta.rowcount," linha deletada com sucesso\n")
        else:
            print("nenhum filme encontrado com o código fornecido")
        conexao.close

        
    def atualizarFilme(self,titulo,genero,duracao,classificacao_indicativa,codigo):
        conexao = self.conexao()
        consulta = conexao.cursor()
        sql = "UPDATE filmes SET titulo = ?, genero = ?, duracao = ?, classificacao_indicativa = ? WHERE codigo = ?"
        campos = (titulo,genero,duracao,classificacao_indicativa,codigo)
        consulta.execute(sql,campos)
        conexao.commit()
        print(consulta.rowcount," linhas(s) atualizadas com sucesso\n")
        conexao.close
            
        