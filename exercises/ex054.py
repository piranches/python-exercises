from datetime import date
anoatual = date.today().year
maioridade = 0
menoridade = 0
for n in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu?'.format(n)))
    idade = anoatual - ano
    if idade>=21:
        maioridade += 1
    else:
        menoridade += 1
print('Ao todo, tivemos {} pessoa(s) maior(es) de idade e {} menor(es) de idade.'.format(maioridade,menoridade))
