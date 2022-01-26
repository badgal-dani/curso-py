"""Faça um programa que lê um número inteiro n. Escrever a soma de todos os
números de 1 até n. Use while.
"""
n = int(input("Informe um número inteiro: "))
i, soma = 1, 0
while i <= n:
    soma += i
    i += 1
print(f"A soma de todos os números entre 1 e {n} é igual a {soma}")
