print('{:-^40}'.format(' MERCADINHO DO PIRES '))
price = float(input('Insira aqui o preço da compra: {}R${}'.format('\033[1;33m','\033[m')))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    pricef = price*0.9
elif opcao == 2:
    pricef = price*0.95
elif opcao == 3:
    pricef = price
    print('Seu pedido ficará 2x de R${:.2f}.'.format(price/2))
elif opcao == 4:
    pricef = 1.2*price
    meses = int(input('Em quantos meses deseja pagar a compra? '))
    print('Seu pedido ficará {}x de R${:.2f} COM JUROS.'.format(meses,pricef/meses))
else:
    pricef=0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!')
print('O valor da compra é R${:.2f}, com o desconto da forma desejada ficará R${:.2f}.'.format(price,pricef))