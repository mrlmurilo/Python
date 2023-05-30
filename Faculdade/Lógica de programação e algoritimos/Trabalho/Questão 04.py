counter = 0

materiais = []

def cadastrarPeca(counter):
    error = True
    while error:
        try:
            nome = str(input('Nome: '))
            fabricante = str(input('Fabricante: '))
            valor = float(input('Valor: '))
            cod = counter

            obj = {
                'nome': nome,
                'fabricante': fabricante,
                'valor': valor,
                'cod': cod    
            }

            materiais.append(obj)

            counter += 1
            error = False
        except:
            print('Nome, fabricante ou valor, incorretos')

    app()

def consultarPeca():
    error = True
    while error:
        print('Opções: ')

        print('1 - Consultar todas as peças')
        print('2 - Consultar peças por código')
        print('3 - consultar peças por fabricante')
        print('4 - retornar')

        try:
            escolha = int(input('Escolha uma ação: '))

            if (escolha > 4 or escolha < 1):
                print('Escolha inválida')
            else:
                error = False
        except:
            print('Escolha inválida')

    if (escolha == 1):
        loop = 1
        for item in materiais:
            print(f'Item {loop}')

            print('------------------------------------')
            print(f'Nome: {item["nome"]}')
            print(f'Fabricante: {item["fabricante"]}')
            print(f'Valor: {item["valor"]}')
            print(f'Cod: {item["cod"]}')
            print('------------------------------------\n')

            #chamada do def principal

        consultarPeca()

    if (escolha == 2):
        error = True
        while error:
            try:
                cod = int(input('Digite o cod do item: '))
                error = False
            except:
                print('Código inválido')

        for item in materiais:
            if item['cod'] == cod:
                print('--------------------------')
                print('Nome: {}'.format(item['nome']))
                print('Fabricante: {}'.format(item['fabricante']))
                print('Valor: {}'.format(item['valor']))
                print('Cod: {}'.format(item['cod']))
                print('--------------------------\n')

                break
        
        consultarPeca()
    if (escolha == 3):
        error = True
        while error:
            try:
                fabricante = str(input('Digite o nome do fabricante: '))
                error = False
            except:
                print('Código inválido')

        search = []
        for item in materiais:
            if (item['fabricante'] == fabricante):
                search.append(item)

        for item in search:
            print('--------------------------')
            print('Nome: {}'.format(item['nome']))
            print('Fabricante: {}'.format(item['fabricante']))
            print('Valor: {}'.format(item['valor']))
            print('Cod: {}'.format(item['cod']))
            print('--------------------------\n')

        consultarPeca()

    if (escolha == 4):
        app()

def removerPeca():
    error = True
    while error:
        try:
            cod = int(input('Digite o código do produto: '))
            error = False
        except:
            print('Código inválido')

    materiais.remove(cod)

    app()

def app():
    print('Bem vindo ao controle de estoque da bicicletaria do Murilo Santos Margonar!')
    print('1 - Cadastrar peças')
    print('2 - Consultar peças')
    print('3 - Remover peças')
    print('4 - Sair')

    error = True
    while error:
        try:
            resposta = int(input('Escolha a opção desejada:'))

            if (resposta == 1):
                cadastrarPeca(counter)
            elif (resposta == 2):
                consultarPeca()
            elif (resposta == 3):
                removerPeca()
            elif (resposta == 4):
                exit()
            
            if (resposta > 5 and resposta < 0):
                print('Escolha inválida')
                error = True
            else:
                error = False
            
        except:
            print('Escolha inválida')

app()
