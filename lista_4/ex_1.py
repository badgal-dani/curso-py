"""Faça um programa que leia números reais. Quando o número digitado for
o número zero o programa deverá apresentar uma lista com todos os
números que foram digitados e sair do laço while.Use while."""
n = 1
lista = []
print("Forneça números reais para colocar em uma lista. Digite '0' quando desejar parar. ")
while n != 0:
    n = float(input(" "))
    if n == 0:
        break
    else:
        lista.append(n)
print(lista)
