inventario = []
resposta = "S"

#adicionar item ao inventário:
while resposta == "S":
    equipamento = [input("Equipamento: "),
                    float(input("Valor: ")),
                    int(input("Número Serial: ")),
                    input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input("Digite \"s\" para continuar: ").upper()

#exibir dados no inventário:
for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ",elemento[3])

#localizar um item no inventário:
busca = input("\nDigite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca == elemento[0]:
        print("Valor..: ", elemento[1])
        print("Serial.: ", elemento[2])

#depreciar itens no inventário:
depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

#excluir um item no inventário:
serial = int(input("\nDigite o serial do equipamento que será excluído: "))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

#exibir dados no inventário:
for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ",elemento[3])

#resumo dos valores no inventário:
valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print("O equipamento mais caro custa: ", max(valores))
    print(" O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de : ", sum(valores))
