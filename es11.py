#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a- O produto do dobro do primeiro com metade do segundo.
#b- A soma do triplo do primeiro com o terceiro.
#c- O terceiro elevado ao cubo.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
nr = float(input("Digite o número real: "))
produto = (n1*2) * n2/2
soma = (n1*3) + (nr)
cubo = nr * 3
print(f"O produto do dobro de {n1} com metade de {nr} é igual a {produto}")
print(f"A soma do triplo de {n1} com {nr} é igual a {soma}")
print(f"O valor {nr} elevado ao cubo vale {cubo}")