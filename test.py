#Projeto Para melhora de lógica matematica

p = [{ 'nome': 'cleiton', 'invI': 10000, 'PontosReunião': 6, 'horatrabalhada': 233, 'div': 0 },{ 'nome': 'jorge', 'invI': 2322, 'PontosReunião': 10, 'horatrabalhada': 233, 'div': 0}]
empresa = {'nome':'MadeInChina', 'lucro': 30000}


def repasseDeLucros():
    qtdSocios = 0
    totalInvestimento = 0
    totalPontos = 0
    totalHoras = 0

    for socio in p:
        investimentoInicial = socio['invI']
        pontos = socio['PontosReunião']
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
        pontos = socio['PontosReunião']
        horas = socio['horatrabalhada']
        pontuacaofinal = socio['div']
        

        
        spInvestimento = investimentoInicial / pInvestimento
        spPontos = pontos / pPontos
        spHoras =  horas / pHoras


        pontuacaofinal = spHoras + spPontos + spInvestimento 
        pontuacaofinal = pontuacaofinal / 3 # 3 é a quantidade de medidas que eu usei no calculo

        lucroRepartido = (empresa['lucro'] * 0.5)  / 100
        lucroRepartido = lucroRepartido * pontuacaofinal

        print(f'----\n{socio['nome']}\nInvestimento: {spInvestimento:.1f}%\nPontuação Média: {spPontos:.0f}%\nHoras: {spHoras:.0f}%\nDireito a lucro: {pontuacaofinal:.1f}%\nGanho: R${lucroRepartido:.2f}')
    
repasseDeLucros()