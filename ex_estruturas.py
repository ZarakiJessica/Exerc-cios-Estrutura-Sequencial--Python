texto = """Operadores de String
Python oferece operadores para processar texto (ou seja, valores de string).
Assim como os números, as strings podem ser comparadas usando operadores de comparação:
==, !=, <, > e assim po diante.
O operador ==, por exemplo, retorna True se as string nos dois lados do operador tiverem o mesmo valor (Perkovic, p. 23, 2016)
"""

print(f"Tamanho do texto = {len(texto)}")
print(texto.upper())
print(texto.replace("i", 'XX'))
lista_palavras = texto.split()
print(f"Tamanho da lista de palavras = {len(lista_palavras)}")
print(f"Quantidade de vezes que string aparece = {texto.count('string')}")
print(f"Quantidade de vezes que strings aparece = {texto.count('strings')}")