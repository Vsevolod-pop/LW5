from math import *
N = input('Введите натуральное число N: ')
while True:
    if N.isdigit() == True:
        N = int(N)
        break
    else:
        N = input('Некорректное число. Пожалуйста, введите натуральное число N: ')
SUMM = sin(1)
SUMMEND = 1/sin(1)
for i in range (2, N+1):
    SUMM += sin(i)
    SUMMEND += 1/SUMM
print ('Результат выражения равен = ', SUMMEND)