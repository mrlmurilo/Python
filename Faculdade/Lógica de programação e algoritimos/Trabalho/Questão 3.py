valor = None
multiplicador_1 = None
multiplicador_2 = None
dimensao = None

cidade1 = 'RS'
cidade2 = 'SR'
cidade3 = 'BS'
cidade4 = 'SB'
cidade5 = 'BR'
cidade6 = 'RB'

def dimensoesObjeto():
    error = True

    while error:
        try:
            altura = int(input('Altura (cm): '))
            comprimento = int(input('Comprimento (cm): '))
            largura = int(input('Largura (cm): '))

            #cotação
            dimensao = altura*comprimento*largura

            if (dimensao < 1000):
                valor = 10
            elif (1000 <= dimensao < 10000):
                valor = 20
            elif (10000 <= dimensao < 30000):
                valor = 30
            elif (30000 <= dimensao < 100000):
                valor = 50
            elif (dimensao >= 100000):
                print('Dimensão da altura alta de mais')
                error = True
            
            if (dimensao < 100000 and dimensao > 0):
                error = False
        except:
            print('Altura, comprimento ou peso inválidos')
            print('Revise os valores e insira novamente')

            error = True
    
    print('Volume: {}'.format(dimensao))
    print('Valor: {}'.format(valor))

    return valor

def rotaObjeto():
    print('Rotas: ')

    print(f'1 - {cidade1}')
    print(f'2 - {cidade2}')
    print(f'3 - {cidade3}')
    print(f'4 - {cidade4}')
    print(f'5 - {cidade5}')
    print(f'6 - {cidade6}')

    #tratamento de erros
    error = True
    while error:
        try:
            response = int(input('Selecione uma das opções acima:'))
        except:
            print('Rota inválida')
        
        if (response < 1):
            print('Rota inválida')
              
        elif (response > 6):
            print('Rota inválida')
        else:
            error = False

        #cotação
        if (response == 1 or response == 2):
            multiplicador_1 = 1
        elif (response == 3 or response == 4):
            multiplicador_1 = 1.2
        elif (response == 5 or response == 6):
            multiplicador_1 = 1.5
        else:
            error = True

    return multiplicador_1

def pesoObjeto():
    peso = None

    error = True
    while error:
        try:
            peso = int(input('Insira o peso (kg): '))

            if (peso <= 0.1):
                multiplicador_2 = 1
            elif( 0.1 <= peso < 1):
                multiplicador_2 = 1.5
            elif( 1 <= peso < 10):
                multiplicador_2 = 2
            elif (10 <= peso < 30):
                multiplicador_2 = 3
            elif( peso >= 30):
                print('Peso alto de mais')
            
            if (peso < 30):
                error = False
        except:
            print('Peso inválido')
            error = True
        
    return multiplicador_2

def cotacao(valor, m1, m2):
    return (valor*m1)*m2

def app():
    print('Bem vindo a companhia de logistica Murilo Santos!')

    dimensao = dimensoesObjeto()
    peso = pesoObjeto()
    rota = rotaObjeto()

    print('Valor para sua encomenda será de: R${}'.format(cotacao(dimensao,peso,rota)))

app()
