nome = input("Digite o nome do colaborador ")
idade = int(input("Informe a idade "))
empresa = input("Para qual empresa ele vai prestar serviço? ")
media_salarial = float(input("Qual a média salarial dele(a)? "))

print("Colaborador(a) cadastrado(a)!")
print("Colaborador(a) " +nome, "possui " +str(idade), "anos")
print("Seu serviço é provido pela empresa " +empresa, "com a média salarial de " +str(media_salarial))