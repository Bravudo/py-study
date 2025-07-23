import requests

# API do Banco Central
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/1?formato=json"
cotacao = requests.get(url).json()


TempoInvestimento = 12
ValorDolar = float(cotacao[0]['valor'].replace(',','.'))
DinheiroParaInvestir = 500 / ValorDolar
Int_DinheiroParaInvestir = int(DinheiroParaInvestir)
print(f'Saldo em Dolar: ${DinheiroParaInvestir:.2f}')
RiscoMedio = 5


ação = [
    #ativos agressivos
    {'nome': 'PALANTIR TECHNOLOGIES INC', 'code': 'PLTR', 'preco': 148.7, 'risco': 7, 'tempo': TempoInvestimento, 'retorno': 13},
    {'nome': 'NVIDIA CORPORATION', 'code': 'NVDA', 'preco': 167.8, 'risco': 7, 'tempo': TempoInvestimento, 'retorno': 9},
    
    #dividendos passivos
    {'nome': 'MAIN', 'code': 'NVDA', 'preco': 64.1, 'risco': 1, 'tempo': TempoInvestimento, 'retorno': 1 }
]


dp = [[0 for w in range(Int_DinheiroParaInvestir + 1)] for i in range(len(ação) + 1)]

for i in range (1, len(ação) + 1):
    preco = int(ação[i-1]['preco'])
    retorno = int(ação[i-1]['retorno'])

    for w in range(Int_DinheiroParaInvestir + 1):
        if preco > w:
            dp[i][w] = dp[i-1][w]
        else:

