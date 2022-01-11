# 1. Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo ou neutro
print("\nA dança dos números.")
x = int(input("Informe um número para brincar: "))
if x < 0:
    print("É um número negativo.")
elif x == 0:
    print("É um número neutro.")
else:
    print("É um número positivo.")

# 2.Faça um programa em linguagem Python que leia dois números inteiros e informe se estes são iguais ou diferentes.
print("\nVerificar se dois números são iguais.")
num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
if num1 == num2:
    print("Os números digitados são iguais.")
else:
    print("Os números digitados são diferentes.")

# 3. Faça um programa em que o usuário informe o salário recebido e o total gasto com despesas. Deverá ser exibido na tela “Gastos dentro do orçamento” caso o valor gasto não
# ultrapasse o valor do salário e “Orçamento estourado” se o valor gasto ultrapassar o valor do salário.
salario_recebido = float(input("\nInforme seu salário: "))
total = float(input("Informe o total de seus gastos: "))
if salario_recebido >= total:
    print("-- Gastos dentro do Orçamento.")
else:
    print("-- Orçamento estourado.")

# 4. Fazer um algoritmo que ao receber o salário atual de um funcionário, calcule o valor do novo salário, reajustado de acordo com a tabela
print("\nCálculo do novo salário")
salario_atual = float(input("Informe o salario atual: "))

if salario_atual < 500:
    salario_novo = salario_atual + (salario_atual * 0.15)
    print(f"Salario com reajuste = {salario_novo}")

elif 500 <= salario_atual <= 1000:
    salario_novo = salario_atual + (salario_atual * 0.10)
    print(f"Salario com reajuste = {salario_novo}")

else:
    salario_novo = salario_atual + (salario_atual * 0.05)
    print(f"Salario com reajuste = {salario_novo}")

# 5. Crie um código em linguagem Python que peça o nome do usuário por meio da função input (). Se o nome for "Optimus Prime", imprima "Bem-vindo, você é um guerreiro de Cybertron". Caso contrário, imprima "Bom dia, NOME".
print("\n----Olá ---- ")
nome = input("Digite seu nome: ")
if nome == "Optimus Prime" or nome == "optimus prime":
    print("Bem-vindo, você é um guerreiro de Cybertron!")
else:
    print(f"Bom dia, {nome}!")

# 6. Escrever um programa em Python para ler um número inteiro e informar se ele é divisível por 5.
numero = int(input("\nInsira um número inteiro para verificar se é divisível por 5: "))
if numero % 5 == 0:
    print(f"O número {numero}, é divisível por 5.")
else:
    print(f"O número {numero}, não é divisível por 5.")

# 7. Escrever um programa em linguagem Python que lê um valor i, inteiro e positivo e 3 valores a, b e c. Se o valor de i é par então calcular e imprimir na tela a média aritmética de a, b e c. Caso contrário, se i>10 então calcular e imprimir na tela a média aritmética e ponderada de a, b e c. Os pesos dos valores são respectivamente 2, 3 e 4.
##### ACRESCENTAR WHILE PARA VERIFICAR VALOR DE I"
i = int(input("\nInsira o valor de i inteiro e positivo: "))
a = int(input("Insira o valor de a: "))
b = int(input("Insira  o valor de b: "))
c = int(input("Insira  o valor de c: "))
if i % 2 == 0:
    media_arit = (a + b + c) / 3
    print(f"Média aritmética: {media_arit}")
elif i > 10:
    media_pond = (2 * a + 3 * b + 4 * c) / (2 + 3 + 4)
    print(f"Média ponderada: {media_pond}")
else:
    print("\U0001F914")

# 8. Escreva um programa em Python para encontrar números entre 100 e 400 (ambos inclusos), onde cada dígito de um número é um número par. Os números obtidos devem ser impressos em sequência separada por vírgulas.
print("\nNúmeros com todos os dígitos pares entre 100 e 400.")
for i in range(100, 401):
    s = str(i)
    if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0:
        print(f"{i}", end=", ")

# 9. Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time) e informe se o resultado foi um empate, se a vitória foi do primeiro time ou do segundo time.
print("\n\n--Placar de um jogo de futebol--")
gols_timeA = int(input("Digite os gols do time A: "))
gols_timeB = int(input("Informe os gols do time B: "))

if gols_timeA == gols_timeB:
    print("O resultado foi um empate.")
elif gols_timeA > gols_timeB:
    print("O time A venceu.")
else:
    print("O time B venceu.")

# 11. Faça um programa em Python para encontrar a mediana de três valores inseridos pelo usuário.
from statistics import median

print("\nMediana de três valores.")
lista = []
for i in range(3):
    num = float(input(f"Digite o {i + 1}º número: "))
    lista.append(num)
print(f"Mediana = {median(lista)}")

# 12. Escreva um programa em Python para calcular o fatorial de qualquer número inteiro.
print("\nFatorial de um número")
factorial = 1
num = int(input("Digite um número para calcular: "))
if num < 0:
    print("Não existe fatorial para número negativo.")
elif num == 0:
    print("O fatorial de 0 é 1.")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"O fatorial de {num} é {factorial}.")

# 13. Faça um programa em Python para calcular a soma e a média de n números inteiros inseridos pelo usuário. Digite 0 para terminar
print("\nInsira os números para o cálculo da média. Digite 0 para sair: ")
contador = 0
soma = 0
num = 1

while num != 0:
    num = int(input(""))
    soma += num
    contador += 1
if contador == 0:
    print("Digite alguns números")
else:
    print(f"Soma dos números = {soma}.")
    print(f"Média = {soma / (contador - 1)}")

""" 14. Obtenha do teclado as dimensões de um reservatório (altura, largura e comprimento, em centímetros) e o consumo médio diário dos utilizadores do reservatório (em litros/dia). 
Assuma que o reservatório esteja cheio, tenha formato cúbico e informe: 
(a) A capacidade total do reservatório, em litros; 
(b) A autonomia do reservatório, em dias; 
(c) A classificação do consumo, de acordo com a quantidade de dias de autonomia: Consumo elevado, se a autonomia for menor que 2 dias; Consumo moderado, se a autonomia estiver entre 2 e 7 dias; Consumo reduzido, se a autonomia maior que 7 dias. """
print("\n-- Resevartório de Água --")

altura = float(input("Digite a altura (cm): "))
largura = float(input("Digite a largura (cm): "))
comprimento = float(input("Digite o comprimento (cm): "))
c_diario = float(input("Digite o valor do consumo médio diário(litros/dia): "))

cap_total = (
    altura * largura * comprimento
) / 1000  # o resultado seria em cm3 por isso, dividimos por mil para passar de cm3 para litros
auton_reser = cap_total / c_diario

print(f"(a) Capacidade do Reservatório = {cap_total} litros.")
print(f"(b) Autonomia do reservatório = {auton_reser} dias.")
# Classificando o consumo
if auton_reser < 2:
    print("(c) Consumo Elevado.")
elif 2 <= auton_reser <= 7:
    print("(c) Consumo Moderado")
elif auton_reser > 7:
    print("(c) Consumo Baixo.")
