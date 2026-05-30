import os
os.system("cls")
nome = input("Qual é o seu nome? ")

nota1 = float(input("Digite a primeira nota "))
nota2 = float(input("Digite a segunda nota "))
nota3 = float(input("Digite a terceira nota "))
             
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("O aluno foi aprovado")
elif media > 4:
    print("Recuperação")
else:
    print("Reprovada")
          
print("A media é:", media)

print("--------------------")
print("|o aluno:", nome)
print("|Ficou com media:", media)
print("--------------------")


