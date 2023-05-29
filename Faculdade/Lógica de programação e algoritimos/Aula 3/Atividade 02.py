#a
idade = int(input("Digite sua idade"))
if (idade > 60 ) :
    print("Direito aos beneficios!")

#b
escudo = int(input("Digite o seu escudo"))
dano = int(input("Digite seu dano"))
if (dano > 10 and escudo == 0) :
    print("você morreu")

#c
direcao = input("Digite uma direção: ")
if (direcao == "norte" or "sul" or "leste" or "oeste") :
    print("Você escapou")