# 1 - A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34... 
# Faça um programa capaz de gerar a série até o N−ésimo termo, 
# onde N é inserido pelo usuário.
n = int(input("Informe n para gerar a sequência de Fibonacci: "))

anterior = 1
proximo = 1
soma = 1
fib = []
fib.append(anterior)
fib.append(proximo)

for i in range(n):
    soma = proximo + anterior
    anterior = proximo
    proximo = soma
    fib.append(soma)

print(f"Sequência: {fib}")
