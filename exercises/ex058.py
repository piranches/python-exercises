import random
x = random.randint(0,10)
count = 1
number = int(input('Digite o seu palpite: '))
while x != number:
    number = int(input('Palpite equivocado, tente novamente: '))
    count += 1
print('Parabéns, você acertou! Para isso, foram necessários {} tentativas.'.format(count))