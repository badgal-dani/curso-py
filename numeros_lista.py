# 4 - Faça um programa que, dado um conjunto de N números, determine o menor valor,
# o maior valor e a soma dos valores.
numeros = [6, 5, 23, 47, 9, 10]
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
soma2 = maior + menor
print(f"Lista de números: {numeros}")
print(f"Menor valor: {menor}\nMaior valor: {maior}\nSoma entre o maior e o menor: {soma2}"
      f"\nSoma dos valores: {soma}")