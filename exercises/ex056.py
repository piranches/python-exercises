idades = 0
nomevelho = ''
idadevelho = 0
contmulher = 0
for p in range(1,5):
    print('{:-^19}'.format(' {}ª PESSOA '.format(p)))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    idades += idade
    if p == 1 and sexo in 'Mm':
        nomevelho = nome
        idadevelho = idade
    if idadevelho<idade and sexo in 'Mm':
        nomevelho = nome
        idadevelho = idade
    if sexo in 'Ff' and idade<20:
        contmulher += 1


print('A média de idade do grupo é de {} anos.'.format(idades/p))
print('O homem mais velho tem {} anos e se chama {}.'.format(idadevelho,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(contmulher))