#Projeto Para melhora de lógica matematica

p = [{ 'nome': 'Cleiton', 'invI': 10000, 'PontosReunião': 6, 'horatrabalhada': 233, 'direito': 0 },
     { 'nome': 'Jorge', 'invI': 2322, 'PontosReunião': 10, 'horatrabalhada': 233, 'direito': 0},
     { 'nome': 'Gustavo', 'invI': 5076, 'PontosReunião':9, 'horatrabalhada': 482, 'direito': 0},
     { 'nome': 'Rafael', 'invI': 7592, 'PontosReunião': 7, 'horatrabalhada': 352, 'direito': 0}]
empresa = {'nome':'MadeInChina', 'lucro': 30000}


def repasseDeLucros():
    totalInvestimento = 0
    totalPontos = 0
    totalHoras = 0

    lucroEmpresa = empresa['lucro']

    for socio in p:
        investimentoInicial = socio['invI']
        pontos = socio['PontosReunião']
        horas = socio['horatrabalhada']

        totalInvestimento += investimentoInicial
        totalPontos += pontos
        totalHoras += horas
    
    print(f'---- Totais Gerais da Empresa {empresa['nome']} ----\nTotal Investimento: {totalInvestimento}. Total Pontos de Reunião: {totalPontos}. Total Horas:{totalHoras}\n')        

    #Porcentagem dos Valores
    pInvestimento = totalInvestimento / 100
    pPontos = totalPontos / 100
    pHoras = totalHoras / 100
    print(f'---- Relatório de Repartição de lucros ----')

    for socio in p:
        nome = socio['nome']
        investimentoInicial = socio['invI']
        pontos = socio['PontosReunião']
        horas = socio['horatrabalhada']
        pontuacaofinal = socio['direito']
        

        
        spInvestimento = investimentoInicial / pInvestimento
        spPontos = pontos / pPontos
        spHoras =  horas / pHoras


        pontuacaofinal = spHoras + spPontos + spInvestimento 
        pontuacaofinal = pontuacaofinal / 3 # 3 é a quantidade de medidas que eu usei no calculo

        # Lucro por Pessoa
        lucroRepartido = (empresa['lucro'] * 0.5)  / 100
        lucroRepartido = lucroRepartido * pontuacaofinal
       
       # Lucro Restante da Empresa
        lucroEmpresa = lucroEmpresa - lucroRepartido
        print(f'\n{socio['nome']}\nInvestimento: {spInvestimento:.1f}%\nReunião: {spPontos:.0f}%\nHoras: {spHoras:.0f}%\nDireito: {pontuacaofinal:.1f}%\nLucro líquido: R${lucroRepartido:.2f}')
    
    print(f'\n---- Dinheiro Restante para a empresa ----\nR${lucroEmpresa:.2f}')
   
   
repasseDeLucros()