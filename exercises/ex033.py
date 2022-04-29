print('Descubra entre três números qual é o maior!')
number1 = float(input('Digite o {}primeiro{} número: '.format('\033[1;33m','\033[m')))
number2 = float(input('Digite o {}segundo{} número: '.format('\033[1;32m','\033[m')))
number3 = float(input('Digite o {}terceiro{} número: '.format('\033[1;35m','\033[m')))
maior = number1
if number1<number2 and number2>number3:
    maior = number2
if number3>number1 and number3>number2:
    maior = number3
menor = number1
if number1>number2 and number2<number3:
    menor = number2
if number3<number1 and number3<number2:
    menor=number3
print('O maior entre eles é o {:.2f}.'.format(maior))
print('O menor entre eles é o {:.2f}.'.format(menor))