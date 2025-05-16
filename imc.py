nome = input("Digite seu nome:")
peso = float(input("Quanto você pesa? "))
altura = float (input("Qual é a sua altura? "))
imc = peso/(altura*peso)
if imc<=18.5:
    print("Você esta abaixo do peso ideal!")
elif imc>= 18.5 and imc<=29.9:
    print ("Você esta no peso ideal")
elif imc>= 25 and imc<=29.9:
    print ("Você esta sobre peso")
else:
    print("Você esta na obesidade")