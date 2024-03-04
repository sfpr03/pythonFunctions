nome = input("informe o nome do paciente")
idade = int(input("Qual a idade do paciente?"))
infeccao = input("Supeito(a) de doença infectocontagiosa?").upper()

if infeccao=="SIM":
    print("O paciente" +nome, "deve ser encaminhado para a sala AMARELA")
elif infeccao=="NAO":
    print("O paciente" +nome, "deve ser encaminhado para a sala BRANCA")
else:
    print("A pergunta sobre a doença infectocontagiosa deve ser respondida com sim ou nao")

if idade>=65:
    print("O paciente possui prioridade")
else:
    genero = input("Qual o gênero do paciente?").upper()
if genero =="FEMININO" and idade>=11:
    gravidez = input("A paciente está grávida?").upper()
    if gravidez=="SIM":
        print("A paciente possui prioridade")
    else:
        print("Paciente sem prioridade")
else:
    print("Paciente sem prioridade")


