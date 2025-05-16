nome = input("Digite seu nome:")
salario_fixo = float(input("Digite o valor do seu salário fixo: R$"))
vendas = int(input("Qual valor mensal de vendas: "))
bonus = 0.15
salario_total = salario_fixo*bonus
if vendas >=20:
    print(f"O seu salario foi de: {salario_total+salario_fixo} voce bateu a meta!")
elif vendas <20:
    print("voce não bateu a meta")