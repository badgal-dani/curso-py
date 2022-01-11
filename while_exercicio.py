""" 1 - Faça um programa que leia um nome de usuário e a sua senha 
e não aceite a senha igual ao nome do usuário, mostrando uma mensagem 
de erro e voltando a pedir as informações.
"""
user = input("Forneça um nome de usuário: ")
while True:
    senha = input("Forneça uma senha diferente do nome de usuário fornecido: ")
    if senha != user:
        print("Nome de usuário e senha criados\U0001F603\n")
        break
    else:
        print("Senha não pode ser igual ao nome de usuário fornecido! Tente novamente.")

""" 2 - Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo 
até que o usuário informe um valor válido.
"""
while True:
    nota = float(input("Forneça uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        print(f"Parabéns! A nota {nota} está dentro do intervalo fornecido.")
        break
    else:
        print("Valor incorreto.")
