#!/usr/bin/python
a = 0
while a <= 100:
    a += 1
    if (a % 3) != 0:
         continue;
    print(str(a))
