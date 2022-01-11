def soma(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


print("\nEscolha qual opção deseja realizar: ")
opcao = input("Digite '+' para selecionar a soma, '-' para selecionar a subtração,"
              "'/' para divisão ou '*' para multiplicação: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if opcao == '+':
    valor_soma = soma(num1, num2)
    print(f"{num1} + {num2} = {valor_soma}")
elif opcao == '-':
    valor_sub = sub(num1, num2)
    print(f"{num1} - {num2} = {valor_sub}")
elif opcao == '/':
    valor_div = div(num1, num2)
    print(f"{num1} / {num2} = {valor_div}")
elif opcao == '*':
    valor_mult = mult(num1, num2)
    print(f"{num1} * {num2} = {valor_mult}")
else:
    print("Vai pra onde?\U0001F928")
