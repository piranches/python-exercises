import time
x = int(input('Primeiro valor: '))
y = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('{:=^30}'.format('LISTA DE OPÇÕES'))
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    print('{:-^30}'.format('ANÁLISE!'))
    time.sleep(1)
    if opcao == 1:
        print('A soma entre {} e {} é {}.'.format(x,y,x+y))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é {}.'.format(x,y,x*y))
    elif opcao == 3:
        if x > y:
            print('O maior valor é {}.'.format(x))
        else:
            print('O maior valor é {}.'.format(y))
    elif opcao == 4:
        x = int(input('Novo primeiro valor: '))
        y = int(input('Novo segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Por favor insira novamente!')
    time.sleep(1)
print('Fim do programa!')