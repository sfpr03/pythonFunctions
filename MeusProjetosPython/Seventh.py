nome = input("Informe o nome do paciente: ")
idade = int(input("Qual a idade do paciente? "))
infeccao = input("O paciente é suspeito de alguma doença infectocontagiosa? ").upper()

while infeccao != "SIM" and infeccao !="NAO":
    print("Digite SIM ou NÃO")
    infeccao = input("O paciente é suspeito de alguma doença infectocontagiosa? ").upper()

if infeccao =="SIM":
    print("Encaminhe o paciente para a sala AMARELA")
else:
    print("Encaminhe o paciente para a sala BRANCA")

if idade >65:
    print("Paciente com prioridade")
else:
    print("Lendo informações de ficha...")
    genero = input("Qual o gênero do paciente?").upper()
    if genero =="FEMININO" and idade >10:
        gravidez = input("A paciente está grávida?").upper()
        if gravidez =="SIM":
            print("A paciente tem prioridade")
        else:
            print("Paciente sem prioridade")


