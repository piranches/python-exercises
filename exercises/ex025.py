from socket import SIO_KEEPALIVE_VALS


name = str(input('Insira um nome: ')).strip()
uppername = name.upper()
if uppername.find('SILVA') == -1:
    print('O nome {} não possui SILVA'.format(uppername))
else:
    print('O nome {} possui SILVA!'.format(uppername))