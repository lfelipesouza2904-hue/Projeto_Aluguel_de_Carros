import os
os.system("cls")

nome = input("Qual é o seu nome? ")
idade = int(input("qual é a sua idade? "))

if idade >= 18:
    possui_carteira = input("Possui carteira de motorista? \n (1-Sim / 2-Não) ")
    if  possui_carteira == "1":
         print("Pode dirigir")
    else:
         print("Não pode dirigir")
else:
     print("Menor de idade")


 