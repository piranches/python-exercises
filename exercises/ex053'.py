frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
aglutinado = ''.join(palavras)
inverso = aglutinado[::-1]
print('O inverso de {} é {}.'.format(aglutinado,inverso))
if aglutinado == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')