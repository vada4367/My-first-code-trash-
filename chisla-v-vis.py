#!/usr/bin/python3.9

#kolcif
kolcif = int(input("какое кол. цифр будет?:"))

#dlya input chisla voprosa
chisloN = 1

#input
n = []
print(n)

for i in range(0, kolcif):
    cifinput = input("число N" + str(chisloN) + ": ")
    n.append(cifinput)
    chisloN = chisloN + 1

    print(cifinput)

#output    
nn = []
print(nn)

for i in range(0, kolcif):
    nn.append(0)
    print(nn)

#chislo
chiszap = -1
print(chiszap)

#zapolnenie output
for i in range(0, kolcif):

    a = 0
    chiszap = chiszap + 1
    chiszap2 = -1
    print(chiszap)
    print(chiszap2)
    
    for i in range(0, kolcif):
        chiszap2 = chiszap2 + 1
        if n[chiszap] > n[chiszap2]:
            print(chiszap2)
            a = a + 1
            print(a)
        print(kolcif)

    nn[a] = n[chiszap]
    print(nn)
    
print(nn)
