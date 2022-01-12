# 2 - Faça um programa que crie uma matriz NxN, insira os valores e 
# imprima em formato de matriz.
n = 3
matriz = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        matriz[i][j] = float(input(f"Informe o valor do elemento [{i + 1}][{j + 1}]: "))
print("\nMatriz:")
for i in range(n):
    print(matriz[i])
