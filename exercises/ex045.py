import random
from secrets import choice
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
pchoice = int(input('Qual é a sua jogada? '))
itens = ['PEDRA','PAPEL','TESOURA']
mchoice = random.randint(0,2)
if itens[pchoice] == itens[mchoice]:
    print("""O computador escolheu {}.\nO jogador escolheu {}.\nPortanto, o jogo EMPATOU!""".format(itens[mchoice],itens[pchoice]))
elif itens[pchoice] == 1 and itens[mchoice] != 1:
    if itens[mchoice] == 2:
        print("""O computador escolheu {}.\nO jogador escolheu {}.\nPortanto, o COMPUTADOR VENCEU!""".format(itens[mchoice],itens[pchoice]))
    else:
        print("""O computador escolheu {}.\nO jogador escolheu {}.\nPortanto, o JOGADOR VENCEU!""".format(itens[mchoice],itens[pchoice]))
elif itens[pchoice] == 2 and itens[mchoice]:
    if itens[mchoice] == 1:
        print("""O computador escolheu {}.\nO jogador escolheu {}.\nPortanto, o JOGADOR VENCEU!""".format(itens[mchoice],itens[pchoice]))
    else:
        print("""O computador escolheu {}.\nO jogador escolheu {}.\nPortanto, o COMPUTADOR VENCEU!""".format(itens[mchoice],itens[pchoice]))
else:
    if itens[mchoice] == 1:
        print("""O computador escolheu {}.\nO jogador escolheu {}.\nPortanto, o COMPUTADOR VENCEU!""".format(itens[mchoice],itens[pchoice]))
    else:
        print("""O computador escolheu {}.\nO jogador escolheu {}.\nPortanto, o JOGADOR VENCEU!""".format(itens[mchoice],itens[pchoice]))
