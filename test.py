produtos = ["Maçã", "Banana", "Pão"]
precos = [2.5, 1.8, 3.0]
quantidades = [3, 5, 2]

total = 0
for i in range(len(produtos)):
    total += precos[i] * quantidades[i]
print(f'Total dos Produtos {total}')