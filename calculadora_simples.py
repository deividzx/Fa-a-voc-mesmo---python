opcao = 0
while opcao !=5:
    print ("===Calculadora===")
    print("1- Adição")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("5- Sair")
    opcao = int(input("Escolha uma opção "))
    if opcao == 1:
        print("Você escolheu adição.")
        numero1 = int(input(" Escolha o primeiro numero: "))
        numero2 = int(input(" Escolha o segundo numero: "))
        resultado_soma= numero1+numero2
        print (f"O resultado da adição é: {resultado_soma}")
    if opcao == 2:
        print("Você escolheu subtração.")
        numero1 = int(input(" Escolha o primeiro numero: "))
        numero2 = int(input(" Escolha o segundo numero: "))
        resultado_subtracao = numero1-numero2
        print (f"O resultado da subtração é:{resultado_subtracao}")
    if opcao == 3:
        print("Você escolheu multiplicação.")
        numero1 = int(input(" Escolha o primeiro numero: "))
        numero2 = int(input(" Escolha o segundo numero: "))
        resultado_multiplicacao = numero1*numero2
        print (f"O resultado da multiplicação é:{resultado_multiplicacao}")
    if opcao == 4:
        print("Você escolheu divisão.")
        numero1 = int(input(" Escolha o primeiro numero: "))
        numero2 = int(input(" Escolha o segundo numero: "))
        resultado_divisao = numero1/numero2
        print (f"O resultado da divisão é:{resultado_divisao}")
    if opcao == 5:
        print("Saindo...")
        break