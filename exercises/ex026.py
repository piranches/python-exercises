from itertools import count
import string
sentence = str(input('Insira uma frase aqui: ')).strip()
uppernewsentence = sentence.translate(str.maketrans('', '', string.punctuation)).upper()
print('A letra A aparece {} vezes na frase.'.format(uppernewsentence.count('A')))
print('A letra A aparece pela primeira vez na posição {}.'.format(uppernewsentence.find('A')+1))
print('A letra A aparece pela ultima vez na posição {}.'.format(uppernewsentence.rfind('A')+1))