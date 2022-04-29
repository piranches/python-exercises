number = int(input('Digite um número: '))
cont = 0
for c in range (1, number+1):
    if number % c == 0:
        cont += 1
        print('{}{}{}'.format('\033[1;32m',c,'\033[m'), end=' ')
    else:
        print('{}{}{}'.format('\033[1;31m',c,'\033[m'), end=' ')
print('\nO número {} foi divisível {} vezes.'.format(number,cont))
if cont == 2:
    print('Por isso, ele É PRIMO!')
else:
    print('Por isso, ele {}NÃO{} É PRIMO!'.format('\033[1;31m','\033[m'))