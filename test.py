import time
import os

def clean():
     os.system('cls' if os.name == 'nt' else 'clear')
def finish_clean():
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')


missoes = [ { 'nome': 'Mundo Corrompido', 'dificuldade': 'Impossível', 'status': 'Pendente','recompensa': 50},
{ 'nome': 'Planeta 02', 'dificuldade': 'facil', 'status': 'Inativo','recompensa': 10},
{ 'nome': 'Tornado Infernal', 'dificuldade': 'Difícil', 'status': 'Inativo','recompensa': 25} ]


MinhasMissoes = []


dado = 0

menuNames = ['List Quest', 'Accept Quest', 'Finish Quest', 'Fail Quest', 'Leave'] 
menu = 0
def system():
    global menu
    clean()  
    while True:
        menu = int(input(f'<><>MENU<><>\n1-{menuNames[0]}\n2-{menuNames[1]}\n3-{menuNames[2]}\n4-{menuNames[3]}\n5-{menuNames[4]}\n<Option><-->'))

        #Listar Todas Missões
        if menu == 1:
            clean() 
            print('--Missões--')
            
            for missao in MinhasMissoes:
                print(f'Missão: {missao['nome']} <> Dificuldade: {missao['dificuldade']}  <> Status: {missao['status']}  <> Recompensa: {missao['recompensa']} ')
                print()
            finish_clean()  
        
        # Listar Missões Pendentes
        if menu == 2:
            clean()   
            print('--Aceitar Missões--')

            for indice, missao in enumerate(missoes):
                    if missao['status'] == 'Pendente' or missao['status'] == 'Inativo':
                        print(f'{indice + 1} - Missão: {missao['nome']} <> Dificuldade: {missao['dificuldade']}')
                        print()
            select = int(input(f'Escolha alguma opção:'))
            if select <= len(missoes):
                 indice = select - 1
                 quest = missoes.pop(indice)
                 quest['status'] = 'Andamento'
                 MinhasMissoes.append(quest)
                 print(f'--> Missão Selecionada: {quest['nome']} - {quest['dificuldade']} - ${quest['recompensa']}')
            finish_clean()  

        if menu == 5:
            print('--Finalizado--')
            break


system()