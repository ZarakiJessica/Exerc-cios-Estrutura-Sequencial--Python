texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeiras letras são: {texto[0:6]}")
print(texto.upper())
print(texto.lower())
print(texto.replace("i", 'XX'))

palavras = texto.split()
print(f"palavras = {palavras}")
print(f"Tamanho de palavras = {len(palavras)}")