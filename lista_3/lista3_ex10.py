# 10. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de 
# qualquer número inteiro entre 1 a 10. O usuário deve informar de 
# qual número ele deseja ver a tabuada.
def tabuada(n: int):
    res = []
    for i in range(1, 11):
        mult = n * i
        res.append(mult)
    return res


n = int(input("Informe um número para calcular sua tabuada: "))
tab = tabuada(n)
print(f"\nTabuada de {n}:")
for i in range(1, 11):
    print(f"{n} X {i} = {tab[i - 1]}")
