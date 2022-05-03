termo = int(input('Insira o termo inicial da PA: '))
r = int(input('Insira a razão da PA: '))
contador = 1
while contador<=10:
    print('{}, '.format(termo), end='')
    termo = termo+r
    contador+=1
print('FIM')