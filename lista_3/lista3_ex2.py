# 2. Faça um Programa que leia 10 números reais, insira em uma lista e
# mostre-os na ordem crescente (use a função sort()).
numeros = []
print("Informar 10 números reais para inseri-los em uma lista e ordená-los.")
for i in range(10):
    num = int(input(f"Forneça o {i + 1}° número: "))
    numeros.append(num)
print(f"Lista = {numeros}")
numeros.sort()
print(f"Lista ordenada: {numeros}")
