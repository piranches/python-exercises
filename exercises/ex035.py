l1 = float(input('Digite o valor do primeiro seguimento: '))
l2 = float(input('Digite o valor do segundo seguimento: '))
l3 = float(input('Digite o valor do terceiro seguimento: '))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('{}SIM{}, estes seguimentos formam um triângulo!'.format('\033[1;32m','\033[m'))
else:
    print('{}NÃO{}, estes seguimento não formam um triângulo!'.format('\033[1;31m','\033[m'))