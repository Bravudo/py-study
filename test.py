p = [{ 'nome': 'cleiton', 'invI': 10000, 'pontuação': 6, 'horatrabalhada': 233 },{ 'nome': 'jorge', 'invI': 2322, 'pontuação': 10, 'horatrabalhada': 233}]

#50% do lucro será repassado aos sócios
empresa = {'nome':'MadeInChina', 'lucro': 23000}

totalInvestimento = 0
totalPontos = 0
totalHoras = 0

for socio in p:
    nome = socio['nome']
    investimentoInicial = socio['invI']
    pontos = socio['pontuação']
    horas = socio['horatrabalhada']

    totalInvestimento += investimentoInicial
    totalPontos += pontos
    totalHoras += horas
    print(socio)
    print(f'Total Investimento: {totalInvestimento}. Total Pontos: {totalPontos}. Total Horas:{totalHoras}')    
