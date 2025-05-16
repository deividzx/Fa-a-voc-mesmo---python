opcao= 0
frances= 0
integral= 0
doceLiso= 0
doceFarofa= 0
paoForma= 0
valorFrances= 0
valorIntegral= 0
valorDoceLiso= 0
valorDoceFarofa= 0
valorForma=0
while opcao!=6:
    print ("----------PADARIA----------")
    print ("[1] Pão Frances")
    print ("[2] Pão Integral")
    print ("[3] Pão Doce Liso")
    print ("[4] Pão Doce Farofa")
    print ("[5] Pão de Forma")
    print ("[6] Fim da compra.")
    print ("----------------------------")
    opcao =int(input("Escolha uma opção:"))
    if opcao == 1:
        frances=int(input("Digite a quantidade de pão frances que você quer: "))
        valorFrances = frances*1.04
    if opcao == 2:
        integral=int(input("Digite a quantidade de pão integral que você quer: "))
        valorIntegral = integral*1.04
    if opcao == 3:
        doceLiso=int(input("Digite a quantidade de pão doce liso que você quer: "))
        valorDoceLiso = doceLiso*1.08
    if opcao == 4:
        doceFarofa=int(input("Digite a quantidade de pão doce farofa que você quer: "))
        valorDoceFarofa = doceFarofa*1.11
    if opcao == 5:
        format= int(input("Digite a quantidade de pão de forma que você quer: "))
        valorForma = paoForma*0.95
    if opcao ==6:
        valortotal = (valorFrances+ valorIntegral + valorDoceLiso + valorDoceFarofa + valorForma)
print("----------RECIBO----------")
if frances>0:
    print (f"Pão francês - Quantidade:{frances}, Valor: R${valorFrances}")
if integral>0:
    print (f"Pão integral - Quantidade:{integral}, Valor: R${valorIntegral}")
if doceLiso>0:
    print (f"Pão doce liso - Quantidade:{doceLiso}, Valor: R${valorDoceLiso}")
if doceFarofa>0:
    print (f"Pão doce farofa - Quantidade:{doceFarofa}, Valor: R${valorDoceFarofa}")
if paoForma>0:
    print (f"Pão de forma - Quantidade:{paoForma}, Valor: R${valorForma}")
print (f"Valor total da compra: R${valortotal}")
    
    
    
    
    
    
    
    
    
    