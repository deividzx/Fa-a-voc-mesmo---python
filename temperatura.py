opcao = 0 
while opcao !=2:
    print ("===Tabela de temperatura convertida===")
    print ("1- Celsius para Fahrenheirt")
    print ("2- Celsius para Kelvin")
    opcao = int(input("Escolha uma das opções: "))
    if opcao == 1:
        temperatura_inicial = float(input("Digite a temperatura em celsius: "))
        temperatura2 = temperatura_inicial * 9/5+32
        print(f"Temperatura em Fahrenheirt: {temperatura2} ")
    elif opcao ==2:
        temperatura_inicial = float(input("Digite a temperatura em celsius:"))
        temperatura3 = temperatura_inicial +273.15
        print(f"Temperatura em kelvin:{temperatura3}")
    else:
        print ("Opção invalida")
        break
    