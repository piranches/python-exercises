l = float(input('Digite a largura da sua parede: '))
h = float(input('Digite a altura da sua parede: '))
s = l * h
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l,h,s))
t = s / 2
print('Para pintar essa parede, você vai precisar de {}L de tinta.'.format(t))