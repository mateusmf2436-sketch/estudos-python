km = int(input('quantos km voce percorreu com seu carro alugado: '))
dias = int(input('quantos dias voce usou seu carro alugado: '))
preco_total = (60*dias)+(0.15*km)
print(f'voce percorreu um total de {km}km em {dias} dias\nassim seu custo total foi de R${preco_total:.2f}')