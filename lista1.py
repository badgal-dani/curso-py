import math

# 1 - Faça um Programa que peça dois números e imprima a soma.
print('\n1 - Efetuando a soma de dois números.')
num1 = float(input('Forneça o primeiro número: '))
num2 = float(input('Forneça o segundo número: '))
soma = num1 + num2
print(f'\nSomando: {num1} + {num2} = {soma}.\n')

# 2 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print('\n2 - Efetuando o calculo da média.')
n = int(input('Informe a quantidade de notas: '))
notas = []
for i in range(n):
    nota = float(input(f'Informe a {i + 1}° nota: '))
    notas.append(nota)
media = sum(notas) / n
print(f'\nA média das {n} notas é de {media}.', end=' ')
if media >= 7:
    print('O/A aluno/a está aprovado/a! :D\n')
else:
    print('O/A aluno/a está reprovado/a :(\n')

# 3 - Faça um Programa que converta metros para centímetros.
print('\n3 - Convertendo de m para cm.')
metro = float(input('Forneça a distância em metros: '))
cm = metro * 100
print(f'\n{metro}m equivalem a {cm}cm.\n')

# 4 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

print('\n4 - Calculando a área de um círculo a partir de seu raio.')
raio = float(input('Informe o raio do círculo em cm: '))
area_c = raio ** 2 * math.pi
print(f'\nA área do círculo é de: {area_c}cm^2.\n')

# 5 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro
# desta área para o usuário.
print('\n5 - Calculando a área de um quadrado e seu dobro.')
lado = float(input('Forneça o tamanho do lado do quadrado em cm: '))
area_q = lado ** 2
dobro = area_q * 2
print(f'\nA área do quadrado é igual a {area_q}cm^2 e seu dobro equivale a {dobro}.\n')

# 6 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
print('\n6 - Cálculo do salário total.')
ganho_hora = float(input('Informe qual o valor da sua hora de trabalho em reais: '))
horas = float(input('Informe quantas horas você trabalhou no mês: '))
salario = ganho_hora * horas
print(f'\nNeste mês seu salário total é de R$ {salario}.\n')

# 7 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e
# mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
print('\n7 - Convertendo a temperatura de graus Fahrenheit para graus Celsius.')
f = float(input('Forneça a temperatura em graus Fahrenheit: '))
c = 5 * ((f - 32) / 9)
print(f'{f}°F equivalem a {c}°C.\n')

# 8 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a- o produto do dobro do primeiro com metade do segundo.
# b- a soma do triplo do primeiro com o terceiro.
# c- o terceiro elevado ao cubo.
print('\n8 - Dois números inteiros e um número real.')
numero1 = int(input('Forneça o primeiro número inteiro: '))
numero2 = int(input('Forneça o segundo número inteiro: '))
numero3 = float(input('Forneça o primeiro número real: '))
a = (numero1 * 2) * (numero2 / 2)
b = (numero1 * 3) + numero3
c = numero3 ** 3
print(f'\nO produto do dobro do primeiro com metade do segundo: {a};\nA soma do triplo do primeiro com o terceiro: {b};'
      f'\nO terceiro elevado ao cubo: {c}.\n')

# 9 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58


# 10 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, utilizando as seguintes fórmulas:
# -Para homens: (72.7*h) - 58
# -Para mulheres: (62.1*h) - 44.7
print('\n10 - Cálculo de peso ideal.')
sexo = str(input('Informe seu sexo utilizando m para masculino e f para feminino: '))
while sexo != 'f' and sexo != 'm':
    sexo = str(input('\nESTÁ INCORRETO SUA PESTE BURRA!!!'
                     '\nPor favor, informe seu sexo utilizando m para masculino e f para feminino: '))

else:
    h = float(input('\nInforme sua altura em metros: '))
    if sexo == 'm':
        p_ideal = (72.7 * h) - 58
    elif sexo == 'f':
        p_ideal = (62.1 * h) - 44.7
    else:
        print('Well I dunno how the fuck we got here')
print(f'\nSeu peso ideal é de {p_ideal}kg.\n')
