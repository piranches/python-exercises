name = str(input('Set a name:')).strip().title().split()
print('Olá, muito prazer!')
print('O seu primeiro nome é: "{}".'.format(name[0]))
print('O seu segundo nome é: "{}".'.format(name[len(name)-1]))
