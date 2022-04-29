soma = 0
cont = 0
for c in range(1,7):
    number = int(input('Digite o {} valor inteiro: '.format(c)))
    if number % 2==0:
        soma += number
        cont += 1
print('Você informou {} números PARES e a soma entre eles é {}.'.format(cont,soma))