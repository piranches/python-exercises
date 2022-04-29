n = str(input('Insira aqui o nome de uma cidade: ')).strip().upper()
x = n.find('SANTO')
if x == 0:
    print('A cidade {} começa com a palavra SANTO!'.format(n))
else:
    print('A cidade {} não começa com a palavra SANTO!'.format(n))