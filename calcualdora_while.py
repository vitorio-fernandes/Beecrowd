# Calculadora usando While

while True:
    try:
        num_1 = int(input("Digite o primeiro número: "))
        num_2 = int(input("Digite o segundo número: "))
        escolha = int(input(" 1- Soma\n 2- Subtração\n 3- Divisão\n 4- Multiplicação"))
        resultado = 0

        if escolha == 1:
            resultado = num_1+num_2
        elif escolha == 2:
            resultado = num_1 - num_2
        elif escolha ==3:
            resultado = num_1/num_2
        elif escolha == 4:
            resultado = num_1 * num_2
        else:
            print("Opção Inválida !\n")
        
        print(resultado)

        sair = input("Digite [s] para sair: ") 
        sair  = sair.lower()
        if sair[0] == "s" :
            print("Encerrando a calculadora .....\n")
            break
    except:
        print("Números Inválidos !\n")