contas = [45, 28, 92]
calculo = [1, 2, 3]
totalquadrada = 0

for number in contas:
    for calc in calculo:
        totalquadrada = number * calc
        print(f'{calc} x {number} = {totalquadrada} ')
    print(f'-------------')