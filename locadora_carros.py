preco_por_dia = 90.0
preco_por_km = 0.20
print ("=== Tabela de preços ===")
print (f"Valor por dia alugado: {preco_por_dia}")
print (f"Valor por km rodado: {preco_por_km}")
dia = int(input("Digite a quantidade de dias que o carro foi alugado:"))
km = float(input("Digite a quantidade de kms percorridos: "))
tota_preco_por_dia = dia*preco_por_dia
total_preco_por_km = km*preco_por_km
total = tota_preco_por_dia+total_preco_por_km
print ("=== Recibo ===")
print (f"Dias alugados: {dia}, valor total a pagar: R${tota_preco_por_dia}")
print(f"Total de kms rodados: {km}, valor total a pagar: R${total_preco_por_km}")
print (f"Total a pagar: R${total}")