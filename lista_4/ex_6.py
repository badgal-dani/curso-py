"""Faça um programa que peça 10 números inteiros, calcule e mostre a
quantidade de números pares e a quantidade de números impares"""
i = 1
pares = 0
impares = 0
while i <= 10:
    n = int(input(f"Informe o {i}° número inteiro: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    i += 1
print(f"Nesse conjunto de números: {pares} são pares e {impares} são ímpares.")
