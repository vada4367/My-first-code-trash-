#!/usr/bin/python3
perevod = int(input("Из какой системы в какую будет идти перевод?\n1. Из 10ичной в 2ичную\n2. Из 2ичной в 10ичную\nНапишите 1 или 2: "))

if perevod == 1:
    dischis = int(input("Введи число: "))

    if dischis == 0:
        print("\n0")

    elif dischis == 4:
        print("\n100")

    elif dischis == -4:
        print("\n-100")

    elif dischis < 0:

        dischis = dischis ** 2
        dischis = dischis ** 0.5
        
        ostatok = dischis % 2
        delenie = dischis // 2

        dvchis = []


        while delenie > 0:
            dvchis.append(int(ostatok))
            ostatok = delenie % 2
            delenie = delenie // 2

        dvchis.append(1)
        dvchis.append("-")
        dvchis.reverse()

        print("")
        print(*dvchis, sep="")
        

    else:
        ostatok = dischis % 2
        delenie = dischis // 2

        dvchis = []


        while delenie > 0:
            dvchis.append(ostatok)
            ostatok = delenie % 2
            delenie = delenie // 2

        dvchis.append(1)
        dvchis.reverse()

        print("")
        print(*dvchis, sep="")


elif perevod == 2:
    chis2 = int(input("\nВведите двоичное число: "))

    n = []
    n2 = []
    n3 = 1

    a = 0
    b = 0
    a = int(a)
    b = int(b)

    #списки
    for d in str(chis2): 
        n.append (int(d))

    for i in range(0, len(n)):
        n2.append(n3)
        n3 = n3 * 2 

    n.reverse()

    #обработки
    for i in range(0, len(n)):
        if n[a] == 0:
            a = a + 1
        elif n[a] == 1:
            b = b + n2[a]
            a = a + 1
    print(b)
