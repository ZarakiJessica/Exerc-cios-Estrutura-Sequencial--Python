#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura
#em graus Celsius. C=5*((F-32)/9).
temperatura = float(input("Digite a temperatura marcada em graus Fahrenheit: "))
celsius = 5*((temperatura-32)/9)
print(f"A temperatura de {temperatura} graus Fahrenheit equivale a {celsius} graus Celsius.")