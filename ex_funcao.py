# 2 - Faça um programa, com uma função que necessite de três argumentos, 
# e que forneça a soma desses três argumentos.
def soma(n1: float, n2: float, n3: float):
    soma = n1 + n2 + n3
    return soma


n1 = float(input("Forneça o primeiro número: "))
n2 = float(input("Forneça o segundo número: "))
n3 = float(input("Forneça o terceiro número: "))
print(f"Soma = {soma(n1, n2, n3)}")
