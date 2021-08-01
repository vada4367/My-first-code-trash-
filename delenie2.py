c = input("число:")

print(1)

print(2)

a = 3

while a <= c:

    n = []

    b = 1

    while b <= a ** 0.5:
        b += 1
        if (a % b):
            continue;
        n.append(b)
    if len(n) == 0:
        print(a)
    a += 1
