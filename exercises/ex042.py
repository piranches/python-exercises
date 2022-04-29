print('Insira três valores para descobrir se é possivel formar um triângulo com eles!')
l1 = float(input('Digite o valor do primeiro seguimento: '))
l2 = float(input('Digite o valor do segundo seguimento: '))
l3 = float(input('Digite o valor do terceiro seguimento: '))
condicionante = l1<l2+l3 and l2<l1+l3 and l3<l1+l2
equilatero = l1==l2==l3
escaleno = l1!=l2!=l3!=l1
isosceles = l1==l2!=l3 or l3==l1!=l2 or l2==l3!=l1
if condicionante:
    print('{}SIM{}, estes seguimentos formam um triângulo '.format('\033[1;32m','\033[m'),end='')
    if equilatero:
        print('EQUILÁTERO!')
    elif isosceles:
        print('ISÓSCELES!')
    elif escaleno:
        print('ESCALENO!')
else:
    print('{}NÃO{}, estes seguimento não formam um triângulo!'.format('\033[1;31m','\033[m'))