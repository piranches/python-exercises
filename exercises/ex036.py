print('Para avaliar o empréstimo bancário é necessario que você responda as seguintes perguntas:')
housep = float(input('Qual é o valor da casa desejada? R$'))
wage = float(input('Qual é o salário do comprador? R$'))
year = float(input('Em quantos anos ele pretende pagar? '))
monthp = housep/year*12
if 0.3*wage<monthp:
    print('O emprestimo será negado!'.format('\033[1;31m','\033[m'))
else:
    print('O emprestimo será {}validado{}!'.format('\033[1;32m','\033[m'))