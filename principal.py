from filme import Filme
filme1 = Filme()
opcao = ("cadastrarFilme","ConsultarFilmes","deletarFilme","atualizarFilme","consultarFilmeindividual","Sair")

while opcao != "Sair" :
    print("                                                BEM VINDO AO CINEMA!!")
    
    print("O que deja fazer?")                             
    print("-"*30)
    print("cadastrarFilme")
    print("-"*30)
    print("ConsultarFilmes")
    print("-"*30)
    print("deletarFilme")
    print("-"*30)
    print("atualizarFilme")
    print("-"*30)
    print("consultarFilmeindividual")
    print("-"*30)
    print("Quero Sair mesmo")
    print("-"*30)
    opcao = input("escolha o que quer fazer: ")
    
    if opcao == "cadastrarFilme":
        titulo = input("Informe o título do filme: ")
        genero = input("Informe o genero do filme: ")
        duracao = int(input("Informe o tempo de filme: "))
        classificacao_indicativa = int(input("informe a classifcacao indicativa"))
        filme1.cadastrarFilme(titulo,genero,duracao,classificacao_indicativa)
        
    elif opcao == "ConsultarFilmes":
        filme1.consultarFilmes()
        


    elif opcao == "deletarFilme":
        codigo = int(input("Codigo do filme: "))
        filme1.deletarFilme(codigo)

    elif opcao == "atualizarFilme":
        codigo = int(input("Codigo do filme"))
        titulo = input("Informe o título do filme: ")
        genero = input("Informe o genero do filme: ")
        duracao = int(input("Informe o tempo de filme: "))
        classificacao_indicativa = int(input("informe a classifcacao indicativa: "))
        filme1.atualizarFilme(titulo,genero,duracao,classificacao_indicativa,codigo)

    elif opcao == "consultarFilmeindividual":
         codigo = int(input("Codigo do filme"))
         filme1.consultarFilmeindividual(codigo)
       
    elif opcao == "Sair":
        print("Flw")
        break

