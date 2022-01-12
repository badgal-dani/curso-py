# 8. Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.(Use range de
# intervalos (range(x, y)))
n1 = int(input("Informe o primeiro número inteiro: "))
n2 = int(input("Informe o segundo número inteiro: "))
if n1 > n2:
    for i in range(n2, n1 + 1):
        print(i)
elif n1 < n2:
    for i in range(n1, n2 + 1):
        print(i)
else:
    print("Ambos os números possuem o mesmo valor, não há números inteiros entre eles.")
    