from math import *
A = input('Введите число А: ')
while True:
    while True:
        if A.isdigit() == True:
            A = int(A)
            break
        else:
            A = input('Число A некорректно, введите другое значение - ')
    B = input('Введите число В: ')
    while True:
        if B.isdigit() == True:
            B = int(B)
            break
        else:
            B = input('Число B некорректно, введите другое значение - ')
    if A < B:
        break
    else:
        print('Введенные числа не подходят под условие А < В')
        A = ''
        B = ''
N = 0
count = 1
for i in range(A,B+1):
    print(count, 'число -', i)
    count += 1
    N += 1
print ('Количество N чисел равно - ', N)