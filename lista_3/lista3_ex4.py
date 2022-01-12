# 4. Faça um Programa que peça o nome, a idade e a altura de N pessoas,
# armazene cada informação em uma lista e depois insira em uma lista maior
# chamada pessoas. Por fim, imprima o nome e altura de cada pessoa, e
# diga se ela é maior ou menor de idade.
n = int(input("\nInforme a quantidade de pessoas: "))
pessoas = []
for i in range(n):
    nome = input(f"Digite o nome da {i + 1}° pessoa: ")
    idade = int(input(f"Digite a idade da {i + 1}° pessoa: "))
    altura = float(input(f"Digite a altura da {i + 1}° pessoa em m: "))
    print()
    nova_pessoa = [nome, idade, altura]
    pessoas.append(nova_pessoa)

for x in pessoas:
    print(f"A/O {x[0]} mede {x[2]}m e", end=' ')
    if x[1] >= 18:
        print("é maior de idade!")
    else:
        print("é menor de idade!")
