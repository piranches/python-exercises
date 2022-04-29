kilometer = int(input('Insira aqui a velocidade do carro em Km/h: '))
tticket = float(7*(kilometer-80))
if kilometer > 80:
    print('Você ultrapassou 80km/h em {}km/h. Isso equivale a uma multa de: R${:.2f}.'.format((kilometer-80),tticket))