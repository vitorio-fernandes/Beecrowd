"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


try:
    hora = int(input("Digite a hora: "))

    dia = hora >= 0 and hora <= 11
    tarde = hora >11 and hora <=17
    noite = hora >=18 and hora <23

    if dia:
        print("Bom dia !\n")
    elif tarde:
        print("Boa tarde !\n")
    elif noite:
        print("Boa Noite !\n")
except:
    print("Digite números inteiro !\n")

