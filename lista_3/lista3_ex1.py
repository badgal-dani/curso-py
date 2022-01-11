# 1. Faça um Programa que leia 5 números inteiros, insira em uma lista e
# mostre-os.
numeros = []
print("Informar 5 números inteiros para inseri-los em uma lista.")
for i in range(5):
    num = int(input(f"Forneça o {i + 1}° número: "))
    numeros.append(num)
print(f"Lista = {numeros}")
