# A partir do ano de nascimento imprimir a idade e dizer se é maior de idade
ano_atual = 2022
nasc = int(input("Informe seu ano de nascimento: "))
idade = ano_atual - nasc
if idade >= 18:
    print(f"Você tem {idade} anos, ou seja, é maior de idade.\n")
else:
    print(f"Você tem {idade} anos, ou seja, é menor de idade.\n")
