maior = 0 
menor = 0
for n in range(1,6):
    peso = float(input('Insira o peso da {}ª pessoa: '.format(n)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg.'.format(menor))