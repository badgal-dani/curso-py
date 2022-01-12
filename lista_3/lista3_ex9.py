# 9. Faça um programa que, dado um conjunto de N números, determine o 
# menor valor, o maior valor e a soma dos valores.
nums = [5, 89, 5, 10, 3, 56, 109, 23, 4, 97]
menor = min(nums)
maior = max(nums)
soma_menor_maior = menor + maior
soma_total = sum(nums)
print(nums)
print(f"Menor valor: {menor}\nMaior valor: {maior}")
print(f"Soma entre o menor e o maior valor: {soma_menor_maior}\n"
      f"Soma entre todos os números da lista: {soma_total}")
