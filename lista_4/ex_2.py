"""Faça um programa que receba um usuário e senha. Se a senha de entrada
for igual ao usuário, deverá ser apresentada a mensagem “Senha Inválida”, e
pedir pro usuário inserir a senha novamente. Quando forem diferentes
imprimir a mensagem “Senha aceita” e sair do laço while. DICA (Use while
True e break). Use while.
"""
user = input("Informe o nome de usuário: ")
while True:
    senha = input("Informe a senha: ")
    if senha == user:
        print("A senha não pode ser igual ao nome de usuário!")
    else:
        print("Senha aceita.")
        break
