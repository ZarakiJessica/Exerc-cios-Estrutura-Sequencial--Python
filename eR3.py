#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite F para feminino ou M para masculino: ").upper()
if letra == 'F':
    print(f"Voce escolheu Feminino!")
elif letra == 'M':
    print("Voce escolheu Masculino!")
else:
    print("Sexo Inválido!")