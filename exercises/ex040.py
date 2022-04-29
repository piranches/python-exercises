grade1 = float(input('Insira aqui a primeira nota do aluno: '))
grade2 = float(input('Insira aqui a segunda nota do aluno: '))
media = (grade1+grade2)/2
if media > 7.0:
    print('O aluno está {}APROVADO{}!'.format('\033[1;32m','\033[m'))
elif 6.9>=media>=5:
    print('O aluno está de {}RECUPERAÇÃO{}!'.format('\033[1;31m','\033[m'))
else:
    print('O aluno está {}REPROVADO{}!'.format('\033[1;31m','\033[m'))