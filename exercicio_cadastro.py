# Crie um programa para cadastrar N pessoas.
# Adicione em uma lista e imprima no final.
n = int(input("Quantas pessoas deseja cadastrar: "))
lista_pessoas = []
for indice in range(n):
    nome = input(f"Digite o nome da {indice + 1}° pessoa: ")
    idade = int(input(f"Digite a idade da {indice + 1}° pessoa: "))
    endereco = input(f"Digite o endereço da {indice + 1}° pessoa: ")
    peso = float(input(f"Digite o peso da {indice + 1}° pessoa em kg: "))
    print()
    nova_pessoa = [nome, idade, endereco, peso]
    lista_pessoas.append(nova_pessoa)

for pessoa in lista_pessoas:
    print(
        f"Bem-vin@ {pessoa[0]}, você tem {pessoa[1]} anos.\nVocê mora em {pessoa[2]}. "
        f"E pesa {pessoa[3]} kg."
    )
    if pessoa[1] >= 18:
        print("Você é maior de idade.\n")
    else:
        print("Você é menor de idade.\n")

else:
    print("A listagem de pessoas foi finalizada!")

print(f"Quantidade de pessoas cadastradas: {len(lista_pessoas)}\n")
