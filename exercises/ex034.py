wage = float(input('Digite o salário: '))
if wage>1250.00:
    print('O valor do salário com aumento é: {}R${:.2f}{}'.format('\033[1;32m',wage*1.1,'\033[m'))
else:
    print('O valor do salário com aumento é: {}R${:.2f}{}'.format('\033[1;32m',wage*1.15,'\033[m'))