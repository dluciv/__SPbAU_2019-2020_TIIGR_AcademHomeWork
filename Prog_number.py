#!/usr/bin/env python3
print('Введите 4-х значное число : ')
Y = int(input())
a = Y // 1000
b = (Y // 100) % 10
c = (Y // 10) % 10
d = Y % 10
Z = a + b + c + d
print('В этом числе:')
print(a ,' - тысяч ; ', b ,' - сотен ; ', c ,' - десятков ; ', d ,' - единиц . ')
print('Сумма разрядов числа равна : ', a ,' + ', b ,' + ', c ,' + ', d ,' = ', Z)
print('Перевертыш этого числа - ', d * 1000 + c * 100 + b * 10 + a)
 