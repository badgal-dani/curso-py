import datetime as dt
import locale
locale.setlocale(locale.LC_ALL, "pt_br")

#1 - Crie um programa que receba o dia, mês e ano de nascimento de uma pessoa.
# Use a biblioteca datatime pra verificar o dia da semana que a pessoa nasceu. 

dia = int(input("Informe seu dia de nascimento: "))
mes = int(input("Informe seu mês de nascimento: "))
ano = int(input("Informe seu ano de nascimento: "))
data_nas = dt.datetime(ano, mes, dia)
dia_sem = data_nas.strftime("%A")
print(f"Você nasceu em um/a {dia_sem}.")
