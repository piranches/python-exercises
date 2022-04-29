age = int(input('Digite a idade - em anos - do atleta desejado: '))
if age<9:
    print('O atleta é MIRIM!')
elif age>=9:
    print('O atleta é INFANTIL!')
elif age>=14:
    print('O atleta é JUNIOR!')
elif age>=19:
    print('O atleta é SÊNIOR!')
else:
    print('O atleta é MASTER!')