# 1. Faça um Programa que peça dois números e imprima o maior deles.
print("\n1 - A partir de dois números imprime qual é o maior. ")
n1 = float(input("Forneça o primeiro número: "))
n2 = float(input("Forneça o segundo número: "))
if n1 > n2:
    print(f"{n1} é maior.\n")
elif n1 < n2:
    print(f"{n2} é maior.\n")
else:
    print("Os números possuem o mesmo valor.\n")

# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo
# ou negativo.
print("\n2 - Informa se o valor fornecido é positivo ou negativo.")
v = float(input("Forneça um número qualquer: "))
if v >= 0:
    print("É positivo.\n")
else:
    print("É negativo.\n")

# 3. Faça um programa pra calcular o IMC e informar qual categoria pertence o
# IMC da pessoa. 
print("\n3 - Calcula o IMC e informa a categoria de acordo.")
peso = float(input("Informe seu peso em kg: "))
altura = float(input("Informe sua altura em m: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é de {imc}.")
if imc < 18.5:
    print("Você está abaixo do peso.\n")
elif 18.5 <= imc < 25:
    print("Você está no peso normal.\n")
elif 25 <= imc < 30:
    print("Você está com sobrepeso.\n")
elif 30 <= imc < 35:
    print("Você está com obesidade grau I.\n")
elif 35 <= imc < 40:
    print("Você está com obesidade grau II.\n")
elif imc <= 40:
    print("Você está com obesidade grau III ou mórbida.\n")
else:
    print("WHAT?!?")

# 4. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido
print("\n4 - Verificando sexo.")
sexo = str(input("Informe o sexo, digite F para feminino e M para masculino: "))
if sexo == 'F':
    print("Feminino.\n")
elif sexo == 'M':
    print("Masculino\n")
else:
    print("Sexo inválido.\n")

# 5. Faça um Programa que verifique se uma letra digitada é vogal ou consoante
print("\n5 - Informa se é vogal ou consoante.")
letra = str(input("Forneça uma letra qualquer: "))
if letra in 'aeiouAEIOU':
    print("É uma vogal.\n")
elif letra in 'bcdfghjklmnpqrstvwxyzçBCDFGHJKLMPQRSTVWXYZÇ':
    print("É consoante.\n")
else:
    print("\U0001F914 \n")

# 6. Faça um programa para a leitura de duas notas parciais de um aluno.
print("\n6 - Leitura de duas notas e mostra se está aprovado ou reprovado.")
nota1 = float(input("Forneça a primeira nota: "))
nota2 = float(input("Forneça a segunda nota: "))
media = (nota1 + nota2) / 2
if media == 10:
    print("Aprovado com Distinção. \U0001F60A \n")
elif media >= 7:
    print("Aprovado.\n")
else:
    print("Reprovado.\n")

# 7. Faça um Programa que leia três números e mostre o maior deles
print("\n7 - Fornece 3 números e imprime o maior.")
num1 = float(input("Forneça o primeiro número: "))
num2 = float(input("Forneça o segundo número: "))
num3 = float(input("Forneça o terceiro número: "))
numeros = [num1, num2, num3]
print(f"O maior número é: {max(numeros)}.\n")

# 8. Faça um Programa que leia três números e mostre o maior e o menor deles.
print("\n8 - Fornece 3 números e imprime o maior e o menor.")
nu1 = float(input("Forneça o primeiro número: "))
nu2 = float(input("Forneça o segundo número: "))
nu3 = float(input("Forneça o terceiro número: "))
numero = [nu1, nu2, nu3]
print(f"O maior número é: {max(numero)}.\n"
      f"O menor número é: {min(numero)}.\n")

# 9. Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
print("\n9 - Forneça o preço de 3 produtos e o mais barato será impresso.")
produtos = {}
p1n = str(input("Qual a marca do primeiro produto: "))
p1v = float(input("Qual o valor do produto {p1n}: "))
p2n = str(input("Qual a marca do segundo produto: "))
p2v = float(input("Qual o valor do produto {p2n}: "))
p3n = str(input("Qual a marca do terceiro produto: "))
p3v = float(input("Qual o valor do produto {p3n}: "))
produtos[p1n] = p1v  # Coloca os nomes e os valores como chaves do dict
produtos[p2n] = p2v
produtos[p3n] = p3v
prod = min(produtos, key=produtos.get)  # Pega o elemento de menor valor no dict
print(f"Deve-se comprar o produto de marca {prod} que custa R$ {produtos[prod]}.\n")

# 10. Faça um Programa que leia três números e mostre-os em ordem decrescente.
print("\n10 - Lê três números e os mostra em ordem crescente.")
nume1 = float(input("Forneça o primeiro número: "))
nume2 = float(input("Forneça o segundo número: "))
nume3 = float(input("Forneça o terceiro número: "))
numbers = [nume1, nume2, nume3]
print(sorted(numbers))

# 11. Faça um Programa que pergunte em que turno você estuda.  Peça para digitar 
# M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" 
# ou "Boa Noite!" ou "Valor Inválido!"
print("\n\n11 - Saudações de acordo com o horário em que se estuda.")
turno = str(input("Informe em que turno você estuda, digite  M para Matutino, V para Vespertino ou"
                  " N para Noturno: "))
if turno == 'M':
    print("Bom dia!\n")
elif turno == 'V':
    print("Boa Tarde!\n")
elif turno == 'N':
    print("Boa Noite!\n")
else:
    print("Valor inválido!\n")

# 12. Faça um Programa que peça um número inteiro e determine se ele é par ou impar
print("\n 12 - Informa se o número é par ou ímpar.")
numb = int(input("Forneça um número inteiro qualquer: "))
if numb % 2 == 0:
    print("O número é par.\n")
else:
    print("O número é ímpar.\n")

# 13. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao 
# longo de um semestre, e calcule a sua média.
print("\n13 - Informe as notas e obtenha o desempenho durante o semestre.")
nota1 = float(input("Forneça a nota 1: "))
nota2 = float(input("Forneça a nota 2: "))
media = (nota1 + nota2) / 2
if 9 <= media <= 10:
    print("Conceito A.\n")
elif 7.5 <= media < 9:
    print("Conceito B.\n")
elif 6.0 <= media < 7.5:
    print("Conceito C.\n")
elif 4.0 <= media < 6:
    print("Conceito D.\n")
elif 0 <= media < 4:
    print("Conceito E.\n")
else:
    print("\U0001F914 \n")

# 14. Faça um Programa que leia um número e exiba o dia correspondente da semana.
print("\n14 - Lê um número e imprime o dia da semana correspondente.")
dia = int(input("Digite 1 para Domingo, 2 para Segunda, 3 para Terça, 4 para Quarta, 5 para Quinta, 6 para Sexta e 7 para Sábado: "))
if dia == 1:
    print("Domingo.\n")
elif dia == 2:
    print("Segunda.\n")
elif dia == 3:
    print("Terça.\n")
elif dia == 4:
    print("Quarta.\n")
elif dia == 5:
    print("Quinta.\n")
elif dia == 6:
    print("Sexta.\n")
elif dia == 7:
    print("Sábado.\n")
else:
    print("Huuum?\U0001F914 \n")

# 15. Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela a bebida escolhida:
print("\n15 - Faz um cardápio e bebidas e pede para o user escolher uma delas.")
cardapio = {1: 'Água', 2: 'Xereps', 3: 'Monster'}
print(f"\n\nMENU\n{cardapio}")
esc = int(input("Informe o número correspondente à bebida que você deseja: "))
print(f"Você escolheu {cardapio[esc]}!")
