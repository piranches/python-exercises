number = int(input('Digite um número: '))
cont = 0
for c in range (1, number+1):
    if number % c == 0:
        cont += 1
        print('\033[1;32m', end=' ')
    else:
        print('\033[1;31m', end=' ')
    print(c, end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(number,cont))
if cont == 2:
    print('Por isso, ele É PRIMO!')
else:
    print('Por isso, ele {}NÃO{} É PRIMO!'.format('\033[1;31m','\033[m'))