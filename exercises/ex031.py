distance = int(input('Enter the desired travel distance in \033[4mkilometers\033[m: '))
if distance > 200:
    price = 0.45*distance
    print('For {}{}km{} it costs {}R${:.2f}{}!'.format('\033[4m',distance,'\033[m','\033[1;33m',price,'\033[m'))
else:
    price = 0.5*distance
    print('For {}{}km{} it costs {}R${:.2f}{}!'.format('\033[4m',distance,'\033[m','\033[1;33m',price,'\033[m'))