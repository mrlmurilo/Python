ru = 4513576
nome = "Murilo dos Santos Margonar"

print("Bem Vindo a Loja do {}".format(nome))
vp = float(input("Entre com o valor do produto"))
quantidade = int(input("Entre com o valor da quantidade"))
valor = vp * quantidade
if (quantidade > 0 and quantidade <10 ) :
    print("Não houve descontos")
elif (quantidade > 9 and quantidade < 100) :
    desconto = valor * 0.05
    valor_desconto = valor - desconto
    print("O valor do produto é de R$:{:.2f}".format(valor))
    print("O valor do produto com desconto é de R$:{:.2f} (desconto de 5%)".format(valor_desconto))
elif (quantidade > 100 and quantidade < 1000) :
    desconto = valor * 0.10
    valor_desconto = valor - desconto
    print("O valor do produto é de R$:{:.2f}".format(valor))
    print("O valor do produto com desconto é de R$:{:.2f} (desconto de 10%)".format(valor_desconto))
elif (quantidade <=1000) :
    desconto = valor * 0.15
    valor_desconto = valor - desconto
    print("O valor do produto é de R$:{:.2f}".format(valor))
    print("O valor do produto com desconto é de R$:{:.2f} (desconto de 15%)".format(valor_desconto))
