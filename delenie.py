#!/usr/bin/python
#нужна переменная а = a + 1 в которой мы будем искать делители и записывать в список n
#нужна переменная b которая будет делителем для a
#нужен список n с помощью которого мы будем знать на сколько чисел делиться переменная a
#нужен цикл для обновления а и n 
#с помощью функции len узнаём кол делителей для переменной a
#если больше двух то не выводим переменную a


a = 2
a = int(a)

b = 2
b = int(b)

n = []
while a <= 10:
    while b <= a / 2:
        if (a % b):
            continue;
        c = a / b
        b = b + 1
        n.append(c)
    a = a + 1
print(n)
