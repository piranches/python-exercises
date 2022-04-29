from re import X


birthyear = int(input('Digite o ano de nascimento: '))
x = 18-birthyear
y = birthyear-18
if birthyear<18:
    print('Ainda não é hora desse jovem se alistar! O tempo exato será daqui {} anos.'.format(x))
elif birthyear==18:
    print('Este é o ano em que o jovem deverá se alistar!')
else:
    print('O tempo de alistamento passou em {} anos! Por favor, procure as entidades responsáveis o mais rápido possível!'.format(y))
