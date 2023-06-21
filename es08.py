#Faça um Programa que pergunte quanto voce ganha por hora e o número de horas trabalhadas no mes.
#Calcule e mostre o total do seu salário no referido mes.
ganhaHora = float(input("Digite quanto voce ganha por hora: "))
horaTrabalhada = float(input("Digite quantas horas voce trabalha no mes: "))
totalmes = horaTrabalhada * ganhaHora
print(f"O total do seu salário no referido mes é de {totalmes}")
