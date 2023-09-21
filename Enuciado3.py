"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
try:
    primeiro_nome = input("Digite seu primeiro nome: ")

    curto = len(primeiro_nome) < 5 and len(primeiro_nome) > 0
    normal = len(primeiro_nome) >=5 and len(primeiro_nome) <=6
    grande = len(primeiro_nome) > 6

    if curto:
        print("Seu nome é curto !\n")
    elif normal: 
        print("Seu nome é normal !\n")
    elif grande:
        print("Seu nome é longo !\n")
    else:
        print("Digite um nome válido !\n")
except:
    print("Digite um nome !\n")