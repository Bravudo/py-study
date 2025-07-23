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
AtivoRiscoAlto = 1 # Risco 7 ao 10
AtivoRiscoMedio = 0 # Risco 3 ao 6
AtivoRiscoBaixo = 4 # Risco 0 ao 2

print(f'Saldo para investimento: ${DinheiroParaInvestir:.2f}')

#O Retorno significa quanto mensalmente ela te devolve em porcentagem.
ação = [
    #ativos agressivos
    {'nome': 'PALANTIR TECHNOLOGIES INC', 'code': 'PLTR', 'preco': 148.7, 'risco': 7, 'tempo': TempoInvestimento, 'retorno': 13},
    {'nome': 'NVIDIA CORPORATION', 'code': 'NVDA', 'preco': 167.8, 'risco': 7, 'tempo': TempoInvestimento, 'retorno': 9},
    {'nome': 'JORGES MEDIA TV', 'code': 'JMT', 'preco': 17.8, 'risco': 10, 'tempo': TempoInvestimento, 'retorno': 14},
    #dividendos passivos
    {'nome': 'MAIN', 'code': 'NVDA', 'preco': 64.1, 'risco': 1, 'tempo': TempoInvestimento, 'retorno': 1 }
]



def MaquinaDeEscolha():
    dinheiro = DinheiroParaInvestir

    #Quanto  em porcentagem comprar de cada ativo
    qtdAtivoPerigo = (DivisaoDeAcoesNaCarteira/10) * (AtivoRiscoAlto)
    qtdAtivoMediano = (DivisaoDeAcoesNaCarteira/10) * (AtivoRiscoMedio) 
    qtdAtivoPassivo = (DivisaoDeAcoesNaCarteira/10) * (AtivoRiscoBaixo) 

    print(f'Ativos\n Alto Risco: {qtdAtivoPerigo:.1f}\n Médio Risco: {qtdAtivoMediano:.1f} Baixo Risco: {qtdAtivoPassivo:.1f}')
    

MaquinaDeEscolha()
