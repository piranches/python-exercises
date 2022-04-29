number = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão dessa PA: '))
for c in range(0,11):
    print('{}a{}{} = {}'.format('\033[1;35m',c,'\033[m',number+razao*c), end=' → ')
print('FIM')