import random

n = []

n2 = []

kolcif = int(input("Введи кол. случ. цифор: "))

for i in range(0, kolcif):
	n.append(random.randint(0, 100))

for i in range(0, kolcif):
	n2.append(random.randint(0, 100))

matrix = []

for o in range(0, kolcif):
	
	n3 = []

	for i in range(0, kolcif):
		
		n3.append(int(n[o] * n2[i]))

	matrix.append(n3)

print(n2)
print(n)

for i in range(len(matrix)):         
    for j in range(len(matrix[i])):  
        print(matrix[i][j], end = ' ')
    print()