#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math  #O módulo math fornece funções matemáticas e constantes pré-definidas.
raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio ** 2
print(f"A área do círculo com raio {raio} é: {area:.2f}")

#A função math.pi é utilizada para obter o valor de pi e o operador ** é usado para elevar o raio ao quadrado.
#A área é armazenada na variável area.