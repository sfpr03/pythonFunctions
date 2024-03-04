usuarios={}
opcao = input("Qual ação deseja realizar? "+
        "<I> Incluir User\n"+
        "<P> Pesquisar User\n"+
        "<E> Excluir User\n"+
        "<L> Listar Users: \n").upper()
while opcao =="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        chave=input("Digite o login: ").upper()
        nome=input("Digite o nome: ")
        data=input("Informe a última data de acesso: ")
        estacao=input("Por onde foi efetuado o último acesso? ")
        usuarios[chave]=[nome, data, estacao]
    opcao=input("O que deseja fazer?\n"+
    "<I> Incluir User\n" +
    "<P> Pesquisar User\n" +
    "<E> Excluir User\n" +
    "<L> Listar Users: \n").upper()
