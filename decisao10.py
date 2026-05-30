import os
os.system("cls")

nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))
turno = input("Digite o turno que você estuda (M-matutino / V-vespertino / N-noturno): ")

if turno == "M" or turno == "m":
    print("Bom Dia!")
elif turno == "V" or turno == "v":
    print("Boa Tarde!")
elif turno == "N" or turno == "n":
    print("Boa Noite!")
else:
    print("Valor Inválido!")

print("--------------------")
print("|Aluno:", nome)
print("|Turno:", turno)
print("--------------------")