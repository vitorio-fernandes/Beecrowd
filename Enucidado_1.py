"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


try:
    numero = int(input("Digite um número inteiro: "))
    definição = numero % 2

    if definição == 0:
        print("Esse número é par !\n")

    else:
        print("Esse número é impar !\n")

except:
    print("O valor digitado não é inteiro !\n")

