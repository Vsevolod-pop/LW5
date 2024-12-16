from math import *
v0 = 0
v0digit = 0
g = 9.81
for i in range(1001, 1000000000):
    if i == 1001:
        v0 = sqrt(i*2*g)
    v0digit = sqrt(i*2*g)
    if v0digit == int(v0digit):
        v0digit = int(v0digit)
        break
print('При таком наименьшем значении скорости v0 =', v0, 'высота H станет больше 1000')
print('При таком целом наименьшем значении скорости v0 =', v0digit, 'высота H станет больше 1000')