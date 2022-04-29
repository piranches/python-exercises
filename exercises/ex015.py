perc = float(input('Insira aqui a quantidade de Km percorridos pelo carro alugado: '))
dias = int(input('Insira aqui a quantidade de dias pelos quais ele foi alugado: '))
p = (dias*60) + (0.15*perc)
print('O preço a pagar pelo aluguel do carro é: R${:.2f}'.format(p))