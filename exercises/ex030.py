from re import M
print('Discover if a number is \033[1;33mEVEN\033[m or \033[1;35mODD\033[m!!')
number = int(input('Insert a number: '))
if number%2 == 0:
    print('The number {} is \033[1;33mEVEN\033[m!'.format(number))
elif number == 0:
    print('The number {} is \033[1;33mEVEN\033[m!'.format(number))
else:
    print('The number {} is \033[1;35mODD\033[m!'.format(number))