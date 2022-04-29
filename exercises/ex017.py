from math import sqrt,pow
co = int(input('Insira aqui o comprimento do cateto oposto: '))
ca = int(input('Insira aqui o comprimento do cateto adjacente: '))
hi = sqrt(pow(co,2)+pow(ca,2))
print('O comprimento da hipotenusa do triângulo retangulo de catetos {} e {} é: {:.0f}'.format(co,ca,hi))
