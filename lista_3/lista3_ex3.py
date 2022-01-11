# 3. Faça um Programa que leia N (peça pro usuário informar o valor de N) notas
# e insira em uma lista, depois percorra a lista e calcule a soma das notas, por
# fim calcule a média (soma dividido por N) e mostre na tela.
n = int(input("Informe a quantidade de notas: "))
notas = []
for i in range(n):
    nota = float(input(f"Forneça a {i + 1}° nota: "))
    notas.append(nota)
soma = sum(notas)
media = soma / n
print(f"A média é: {media}.")
