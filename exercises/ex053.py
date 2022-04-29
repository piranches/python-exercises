frase = str(input('Digite uma frase: ')).upper().strip()
listfrase = frase.split()
joinfrase = ''.join(listfrase)
inverso = ''
for letra in range(len(joinfrase)-1,-1,-1):
    inverso += joinfrase[letra]
print('O inverso de {} é {}.'.format(joinfrase,inverso))
if joinfrase == inverso:
    print('Portanto, a frase é um palíndromo!')
else:
    print('Portanto, a frase NÃO É um palíndromo!')