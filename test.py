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

def regradetres():
    a = float(input('[X] []\n [] [?]\nDigite o Numero do X: '))
    b = float(input (f'{int(a)} [X]\n [] [?]\nDigite o Numero do X:'))
    c = float(input (f'{int(a)} {int(b)}\n [X] [?]\nDigite o Numero do X:'))
    print(f'{int(a)} {int(b)}\n{int(c)} [?]')
    print('1. Direta\n2. Inversa')
    option = input('Escolha o tipo de conta: ')

    if option == '1':
        d = c * b / a
        print(f'Resultado: {int(d)}')
    if option == '2':
        d = a * b / c
        print(f'Resultado: {int(d)}')
regradetres()
    