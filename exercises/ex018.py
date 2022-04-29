from cmath import cos
import math
a = float(input('Insira o ângulo desejado: '))
sin = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O seno, cosseno e tangente do ângulo {}° é, respectivamente: {:.3f}, {:.3f} e {:.3f}.'.format(a,sin,cos,tan))