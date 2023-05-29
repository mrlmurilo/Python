a = int(input("Digite um valor"))
b = int(input("Digite um valor"))
c = int(input("Digite um valor"))

if (a and b and c) > 0:
    if (a + b > c) and (a + c > b) and (b + c > a) :
        if (a == b and b == c):
            triangulo = "Equilatero"
        elif (a == b or c):
            triangulo = "Isósceles"
        elif (a != b and b != c):
            triangulo = "Escaleno"
    else:
        print("Ao menos um dos valores indicados não servem para formar um triângulo")
else:
    print("Ao menos um dos valores indicados não servem para formar um triângulo")

print(triangulo)