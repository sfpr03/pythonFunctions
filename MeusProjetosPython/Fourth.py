nome = input("Digite o nome ")
idade = int(input("Digite a idade "))
prioridade = "Não"
if idade>=65:
    print("O paciente " +nome, "tem atendimento prioritário!")
else:
    print("O paciente " +nome, "não tem atendimento prioritário!")
