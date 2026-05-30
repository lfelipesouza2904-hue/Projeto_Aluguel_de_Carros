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

if numero1 < numero2:
    menor = numero1
else:
    menor = numero2

if numero3 < menor:
    menor = numero3

print("O maior numero é:", maior)
print("O menor numero é:", menor)