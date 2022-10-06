from math import sin, cos, tan, radians
r = float(input('Digite um ângulo: '))
a = radians(r)
s = sin(a)
c = cos(a)
t = tan(a)
print('Em relação ao ângulo {}º seu seno vale {:.2f}, seu cosseno vale {:.2f} e sua tangente vale {:.2f}'.format(r, s, c, t))

