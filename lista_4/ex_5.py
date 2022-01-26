"""Faça um programa que lê um número inteiro n. E verifique se n é um número
par, se não for pedir para inserir outro número até que seja par. Use while."""

while True:
    n = int(input("Informe um número inteiro: "))
    if n % 2 == 0:
        print(f"O número {n} é par.")
        break
    else:
        print(f"O número {n} não é par.")
