ru = 4513576
nome = "Murilo dos Santos Margonar"

valor = 0
while True:
    print("Bem vindo a lanchonete do {} com o RU {}".format(nome,ru))
    print(22*("*") + "CARDÁPIO" + 22*("*"))
    print("|COD|" + 15*(" ") + "DESCRIÇÃO" + 15*(" ") + "|VALOR|")
    print("|100|" + 12 * (" ") + "Cachorro Quente" + 12 * (" ") + "| 9,00|")
    print("|101|" + 10 * (" ") + "Cachorro Quente Duplo" + 8 * (" ") + "|11,00|")
    print("|102|" + 18 * (" ") + "X-Egg" + 16 * (" ") + "|12,00|")
    print("|103|" + 17 * (" ") + "X-Salada" + 14 * (" ") + "|12,00|")
    print("|104|" + 17 * (" ") + "X-Bacon" + 15 * (" ") + "|14,00|")
    print("|105|" + 17 * (" ") + "X-Tudo" + 16 * (" ") + "|17,00|")
    print("|200|" + 11 * (" ") + "Refrigerante lata" + 11 * (" ") + "| 5,00|")
    print("|201|" + 15 * (" ") + "Chá Gelado" + 14 * (" ") + "| 4,00|")
    produto = int(input("Digite o código do produto: "))
    if (produto == 100):
        valor += 9.00
        print("Você pediu um Cachorro-Quente no valor de 9,00")
    elif (produto == 101):
        valor += 11.00
        print("Você pediu um Cachorro-Quente Duplo no valor de 11,00")
    elif (produto == 102):
        valor += 12.00
        print("Você pediu um X-Egg no valor de 12,00")
    elif (produto == 103):
        valor += 12.00
        print("Você pediu um X-Salada no valor de 12,00")
    elif (produto == 104):
        valor += 14.00
        print("Você pediu um X-Bacon no valor de 14,00")
    elif (produto == 105):
        valor += 17.00
        print("Você pediu um X-Tudo no valor de 17,00")
    elif (produto == 200):
        valor += 5.00
        print("Você pediu um Refrigerante Lata no valor de 5,00")
    elif (produto == 201):
        valor += 4.00
        print("Você pediu um Chá Gelado no valor de 4,00")
    else:
        print("Opção Invalida")
    print("Deseja pedir mais alguma coisa ?")
    print("1 - Sim")
    print("0 - Não")
    x = int(input())
    if (x == 1):
        continue
    if  (x == 0):
        print("Sua compra deu {}".format(valor))
        break
    else:
        print("Opção inválida, tente novamente.")