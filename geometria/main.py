import area as a

x = int(input("Digite '1' se deseja calcular a área de um círculo, "
              "ou digite '2' se deseja calcula a área de um quadrado: "))

if x == 1:
    r = float(input("Qual o raio do círculo em cm: "))
    area = a.circulo(r)
    print(F"A área do círculo é igual a {area}.")
elif x == 2:
    l = float(input("Qual o lado do quadrado em cm: "))
    area = a.quadrado(l)
    print(F"A área do quadrado é igual a {area}.")
else:
    print("Valor inválido.")
    