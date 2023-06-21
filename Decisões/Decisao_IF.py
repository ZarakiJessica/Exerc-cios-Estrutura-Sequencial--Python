nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
if idade >= 65:
    print(f"O paciente {nome} POSSUI atendimento prioritário!")
else:
    print(f"O paciente {nome} NÃO possui atendimento prioritário!")
print("FIM")