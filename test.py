import sys


def calculadora():
    print ('1. soma \n2. Subtração \n3. Multiplicação\n4. Divisão \n5. Potenciação')
    option = input('Escolha entre 1 e 4:')
    a = float(input('Primeiro Numero: '))
    b = float(input('Segundo Numero: '))

    if option == "1":
        print(f'Resultado {a + b}')
    elif option == "2":
        print(f'Resultado {a - b}')
    elif option == "3":
        print(f'Resultado {a * b}')
    elif option == "4":
        print(f'Resultado {a / b}')
    elif option == "5": 
        print(f"Resultado {a ** b}")
    else: 
        print('Opção Inválida')
calculadora()