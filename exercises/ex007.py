from socket import INADDR_UNSPEC_GROUP


n1 = float(input('Insira a nota de física do primeiro bimestre:'))
n2 = float(input('Insira a nota de física do segundo bimestre:'))
n3 = float(input('Insira a nota de física do terceiro bimentre:'))
n4 = float(input('Insira a nota de física do quarto bimestre:'))
s = n1+n2+n3+n4
print('A média do aluno foi de: {}'.format(s/4))