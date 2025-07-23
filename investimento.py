import requests

# API do Banco Central
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/1?formato=json"
cotacao = requests.get(url).json()
ValorDolar = float(cotacao[0]['valor'].replace(',','.'))

DinheiroParaInvestir = int(1000) / ValorDolar
print(f'Arredondamento: ${int(DinheiroParaInvestir)}')

#perfil
TempoInvestimento = 12
Int_DinheiroParaInvestir = int(DinheiroParaInvestir)
# Risco: 0 a 10
RiscoMedio = 5

print(f'Saldo Total: ${DinheiroParaInvestir:.2f}')


ação = [
    #ativos agressivos
    {'nome': 'PALANTIR TECHNOLOGIES INC', 'code': 'PLTR', 'preco': 148.7, 'risco': 7, 'tempo': TempoInvestimento, 'retorno': 13},
    {'nome': 'NVIDIA CORPORATION', 'code': 'NVDA', 'preco': 167.8, 'risco': 7, 'tempo': TempoInvestimento, 'retorno': 9},
    #dividendos passivos
    {'nome': 'MAIN', 'code': 'NVDA', 'preco': 64.1, 'risco': 1, 'tempo': TempoInvestimento, 'retorno': 1 }
]

def Escolha():
    qtdEscolhas = 0

    for acao in ação:
        preco = acao['preco']
        qtdEscolhas += preco    
    qtdEscolhas = int(qtdEscolhas) / len(ação)
    media = DinheiroParaInvestir / int(qtdEscolhas) 
    print((media))

Escolha()