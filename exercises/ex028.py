import random
from tkinter import Y
print('Pense em um número inteiro de 0 a 5.')
numbers = [0,1,2,3,4,5]
x = int(input('Digite o número escolhido: '))
y = int(random.choice(numbers))
if y == x:
    print('Parabéns, você venceu!')
else:
    print('O numero sorteado foi: {}. Infelizmente, você perdeu.'.format(y))