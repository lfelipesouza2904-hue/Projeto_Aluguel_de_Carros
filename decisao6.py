import os
os.system("cls")

numero1 = int(input("Digite o Primeiro numero: "))
numero2 = int(input("Digite o Segundo numero: "))
numero3 = int(input("Digite o Terceiro numero: "))

if numero1 > numero2:
    maior = numero1
else:
    maior = numero2

if numero3 > maior:
    maior = numero3
    
print("O maior numero é:", maior)