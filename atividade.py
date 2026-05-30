numero = int(input("Digite o primeiro numero da tabuada: "))
inicio = int(input("Digite onde a tabuada começa: "))
final = int(input("Digite onde a tabuada termnina: "))

for multiplicador in range(inicio, final +1):
    print(numero * multiplicador) 