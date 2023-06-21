#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
# cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

metros_quadrados = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

litros_tinta = metros_quadrados / 6  # Considerando a cobertura de 1 litro para cada 6 metros quadrados
litros_tinta += litros_tinta * 0.1  # Acrescentando 10% de folga

latas_tinta = math.ceil(litros_tinta / 18)  # Latas de 18 litros
preco_latas = latas_tinta * 80

galoes_tinta = math.ceil(litros_tinta / 3.6)  # Galões de 3,6 litros
preco_galoes = galoes_tinta * 25

# Misturar latas e galões
latas_mistura = int(litros_tinta // 18)
resto_litros = litros_tinta % 18
galoes_mistura = math.ceil(resto_litros / 3.6)
preco_mistura = latas_mistura * 80 + galoes_mistura * 25

print("Situação 1: Comprar apenas latas de 18 litros")
print("Quantidade de latas a serem compradas:", latas_tinta)
print("Preço total: R$", preco_latas)

print("\nSituação 2: Comprar apenas galões de 3,6 litros")
print("Quantidade de galões a serem comprados:", galoes_tinta)
print("Preço total: R$", preco_galoes)

print("\nSituação 3: Misturar latas e galões")
print("Quantidade de latas a serem compradas:", latas_mistura)
print("Quantidade de galões a serem comprados:", galoes_mistura)
print("Preço total: R$", preco_mistura)