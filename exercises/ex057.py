fruta = str(input('Escolha entre laranja ou maçã: [L/M] ')).upper().strip()[0]
while fruta not in 'ML':
    fruta = str(input('Dados inválidos. Informe novamente: ')).strip().upper()[0]
print('A fruta escolhida foi {}.'.format(fruta))