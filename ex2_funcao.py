# 3 - Faça uma função que receba uma lista, percorra a lista e some
# a quantidade de números pares dessa lista e retorne a soma.
# Imprimir a lista e o resultado da soma ao final do código.
def soma_pares(numeros: list):
    qnt = 0
    for i in numeros:
        if i % 2 == 0:
            qnt += 1
    return qnt


lista = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 8, 10, 12]
qntd = soma_pares(lista)
print(f"Lista = {lista}")
print(f"Quantidade de números pares: {qntd}")
