p = [{ 'nome': 'cleiton', 'invI': 10000, 'pontuação': 6, 'horatrabalhada': 233, 'div': 0 },{ 'nome': 'jorge', 'invI': 2322, 'pontuação': 10, 'horatrabalhada': 233, 'div': 0}]
#50% do lucro será repassado aos sócios
empresa = {'nome':'MadeInChina', 'lucro': 30000}


def repasseDeLucros():
    qtdSocios = 0
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
        qtdSocios += 1

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
        pontuacaofinal = socio['div']
        

        
        spInvestimento = investimentoInicial / pInvestimento
        spPontos = pontos / pPontos
        spHoras =  horas / pHoras


        pontuacaofinal = spHoras + spPontos + spInvestimento 
        pontuacaofinal = pontuacaofinal / 3 # 3 é a quantidade de medidas que eu usei no calculo

        lucroRepartido = empresa['lucro'] / 100
        lucroRepartido = lucroRepartido * pontuacaofinal

        print(f'----\n{socio['nome']}\nInvestimento: {spInvestimento:.2f}%\nPontuação Média:{spPontos:.2f}%\nHoras: {spHoras:.2f}%\nDireito a lucro: {pontuacaofinal:.2f}%\nGanho: R${lucroRepartido:.2f}')
    
        





repasseDeLucros()