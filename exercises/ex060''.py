number = int(input('Digite um número para ver o seu Fatorial: '))
acumulador = 1 
for number in range(number,0,-1):
    acumulador *= number
print('O produto de todos os números é {}.'.format(acumulador))