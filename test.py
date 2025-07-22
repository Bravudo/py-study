p = [{ 'nome': 'cleiton', 'invI': 10000, 'pontuação': 6, 'horatrabalhada': 233 },{ 'nome': 'jorge', 'invI': 2322, 'pontuação': 10, 'horatrabalhada': 233}]
#50% do lucro será repassado aos sócios
empresa = {'nome':'MadeInChina', 'lucro': 30000}


def repasseDeLucros():

    totalInvestimento = 0
    totalPontos = 0
    totalHoras = 0

    for socio in p:
        investimentoInicial = socio['invI']
        pontos = socio['pontuação']
        horas = socio['horatrabalhada']

        totalInvestimento += investimentoInicial
        totalPontos += pontos
        totalHoras += horas

    print(f'Total Investimento: {totalInvestimento}. Total Pontos: {totalPontos}. Total Horas:{totalHoras}')        


    #Porcentagem dos Valores
    pInvestimento = totalInvestimento / 100
    pPontos = totalPontos / 100
    pHoras = totalHoras / 100

    for socio in p:
        nome = socio['nome']
        investimentoInicial = socio['invI']
        pontos = socio['pontuação']
        horas = socio['horatrabalhada']
        

        
        spInvestimento = investimentoInicial / pInvestimento

        spPontos = pontos / pPontos
 
        spHoras =  horas / pHoras
        print(f'----\n{socio['nome']}\nInvestimento: {spInvestimento:.2f}%\nPontuação Média:{spPontos:.2f}%\nHoras: {spHoras:.2f}%')





repasseDeLucros()