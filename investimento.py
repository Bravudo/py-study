import requests

# API do Banco Central
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/1?formato=json"
cotacao = requests.get(url).json()
ValorDolar = float(cotacao[0]['valor'].replace(',','.'))




#Perfil
TempoInvestimento = 12
DinheiroParaInvestir = int(1000) / ValorDolar
DivisaoDeAcoesNaCarteira = 6 # Quantidade de Ações diferentes em sua carteira

# Completar A lista proporcionalmente em quanto você quer que cada area da sua carteira tenha de risco
# Risco: 0 a 10 - Completar até o total de 10
AtivoRiscoAlto = 5 # Risco 7 ao 10
AtivoRiscoMedio = 2 # Risco 3 ao 6
AtivoRiscoBaixo = 3 # Risco 0 ao 2

print(f'Saldo para investimento: ${DinheiroParaInvestir:.2f}')

#O Retorno significa quanto mensalmente ela te devolve em porcentagem.
ação = [
    #ativos agressivos
    {'nome': 'PALANTIR TECHNOLOGIES INC', 'code': 'PLTR', 'preco': 148.7, 'risco': 8, 'tempo': TempoInvestimento, 'retorno': 13},
    {'nome': 'NVIDIA CORPORATION', 'code': 'NVDA', 'preco': 167.8, 'risco': 7, 'tempo': TempoInvestimento, 'retorno': 9},
    {'nome': 'JORGES MEDIA TV', 'code': 'JMT', 'preco': 17.8, 'risco': 10, 'tempo': TempoInvestimento, 'retorno': 14},
    #dividendos passivos
    {'nome': 'MAIN', 'code': 'NVDA', 'preco': 64.1, 'risco': 1, 'tempo': TempoInvestimento, 'retorno': 1 }
]



def MaquinaDeEscolha():
    dinheiro = DinheiroParaInvestir

    DinheiroAlto = (dinheiro / 100) * (AtivoRiscoAlto * 10)
    DinheiroMedio = (dinheiro / 100) * (AtivoRiscoMedio * 10)
    DinheiroBaixo = (dinheiro / 100) * (AtivoRiscoBaixo * 10)

    print(int(DinheiroAlto))

    #Quanto  em porcentagem comprar de cada ativo
    qtdAtivoAlto = (DivisaoDeAcoesNaCarteira/10) * (AtivoRiscoAlto)
    qtdAtivoMedio = (DivisaoDeAcoesNaCarteira/10) * (AtivoRiscoMedio) 
    qtdAtivoBaixo = (DivisaoDeAcoesNaCarteira/10) * (AtivoRiscoBaixo) 

    EscolhaDeAcoes(qtdAtivoAlto, DinheiroAlto)



    print(f'Quantidade de Ativos\n Alto Risco: {qtdAtivoAlto:.1f}\n Médio Risco: {qtdAtivoMedio:.1f}\n Baixo Risco: {qtdAtivoBaixo:.1f}')




def EscolhaDeAcoes(qtdAtivo, qtdDinheiro):
    Nome = ação[0]['nome']
    print(Nome)



MaquinaDeEscolha()



#Comprar Ações de uma lista proporcionalmente a quantidade de risco escolhido por cada ativo
#Separar pela quantidade de ações diferentes definidas para escolher
#Separar por riscos
#Escolher o melhor retorno 