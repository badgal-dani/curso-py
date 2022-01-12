# 6. Faça um programa que leia 5 números e informe o maior número. (Dica: 
# Use lista, função .sort() e indexação negativa (pegar i item [-1]))
nums = []
for i in range(5):
    n = float(input(f"Forneça o {i + 1}° número: "))
    nums.append(n)

print(f"O maior número é: {max(nums)}")
