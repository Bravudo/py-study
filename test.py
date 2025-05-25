calculo = [1, 2, 3]
contas = [45, 28, 92]
totalquadrada = 0

for calc in calculo:
    for number in contas:
        totalquadrada = number * number
    print(f'{contas} x {contas} {totalquadrada} - ')