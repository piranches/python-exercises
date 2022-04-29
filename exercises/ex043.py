peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso/altura**2
print('O IMC dessa pessoa é: {:.2f}'.format(imc))
if imc<18.5:
    print('Cuidado, você está ABAIXO DO PESO ideal!')
elif imc<24.9:
    print('Parabéns, você está na faixa de PESO NORMAL!')
elif imc<29.9:
    print('Cuidado, você está na faixa de SOBREPESO!')
elif imc<30:
    print('Muito cuidado, você está na faixa OBESIDADE GRAU I!')
elif imc<39.9:
    print('Muito cuidado, você está na faixa OBESIDADE GRAU II!')
else:
    print('Muito cuidado, você esta na faixa de OBESIDADE GRAU III ou MÓRBIDA!')