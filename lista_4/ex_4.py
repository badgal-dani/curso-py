"""Faça um programa para ler um número inteiro n. Escrever a soma de todos
os números pares de 2 até n. Use while."""

n = int(input("Informe um número inteiro: "))
i, soma = 1, 0
while i <= n:
    if i % 2 == 0:
        soma += i
    i += 1
print(f"A soma de todos os números pares entre 1 e {n} é igual a {soma}")
