#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = int(input("Digite um valor: "))
if valor > 0:
    print(f"o valor {valor} é positivo!")
elif valor < 0:
    print(f"O valor {valor} é negativo!")
else:
    print(f"O valor é ZERO!")