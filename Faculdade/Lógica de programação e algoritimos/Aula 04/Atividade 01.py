x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o primeiro valor: "))
cont = 1
multi = 0
while (cont <= x) :
    multi = multi + y
    cont = cont + 1
print("resultado da multiplicação: {}x{}={}".format(x, y, multi))