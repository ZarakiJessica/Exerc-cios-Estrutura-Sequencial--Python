#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#utilizando as seguintes fórmulas:
#Para homens: (72.7*h)-58
#Para mulheres: (62.1*h)-44.7
altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite qual seu sexo: ")
if sexo.upper() == 'F':
    peso = (62.1*altura)-44.7
    print(f"O peso ideal para uma mulher com a altura de {altura} metros é de: {peso} quilos.")
elif sexo.upper() == 'M':
    peso = (72.7*altura)-58
    print(f"O peso ideal para um homem com a altura de {altura} metros é de: {peso} quilos.")
else:
    print(f"Sexo inválido! Por favor digite 'F' para feminino e 'M' para masculino.")