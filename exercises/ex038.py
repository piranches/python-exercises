number1 = int(input('Insira um número inteiro: '))
number2 = int(input('Insira um segundo número inteiro: '))
if number1>number2:
    print('O {}primeiro valor{} é o maior entre eles!'.format('\033[1;35m','\033[m'))
elif number1<number2:
    print('O {}segundo valor{} é o maior entre eles!'.format('\033[1;33m','\033[m'))
else:
    print('{}Não existe{} valor maior, os dois são iguais!'.format('\033[1;31m','\033[m'))