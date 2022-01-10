"""1 - Crie um programa que tenha uma lista de 5 frutas, e 
depois adicione uma nova fruta no final da lista. 
Depois remova o primeiro elemento da lista e por fim, 
altere o valor do item 2 pra 'banana'."""
frutas = ['morango', 'maçã', 'abacaxi', 'uva', 'melância']
print(frutas)
fruta = input("Informe uma fruta: ")
frutas.append(fruta)  # Add o elemento fruta
print(frutas)
frutas.pop(0)
print(frutas)
frutas[1] = 'banana'
print(frutas)
