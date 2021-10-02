import random
import numpy as np

def printm(mat):
	for i in range(len(mat)):
	    for j in range(len(mat[i])):
	        print(mat[i][j], end = ' ')
	    print()

def plusmat(mat1, mat2):
	A = np.array(mat1)

	B = np.array(mat2)

	C = (A.T + B).T

	C = np.array(C).tolist()

	printm(C)

def minusmat(mat1, mat2):
	A = np.array(mat1)

	B = np.array(mat2)

	C = (A.T - B).T

	C = np.array(C).tolist()

	printm(C)

def umnmat(mat1, mat2):
	A = np.array(mat1)

	B = np.array(mat2)

	C = (A.T * B).T

	C = np.array(C).tolist()

	printm(C)

def delemat(mat1, mat2):
	A = np.array(mat1)

	B = np.array(mat2)

	C = (A.T % B).T

	C = np.array(C).tolist()

	printm(C)

def rand(sp):
	for i in range(0, kolcif):
		sp.append(random.randint(0, 100))


n = []

n2 = []

kolcif = int(input("Введи кол. случ. цифор: "))

rand(n)

rand(n2)

matrix = []

for o in range(0, kolcif):

	n3 = []

	for i in range(0, kolcif):

		n3.append(int(n[o] * n2[i]))

	matrix.append(n3)

print(n2)
print(n)

print()

printm(matrix)

n = []

n2 = []

kolcif = int(input("Введи кол. случ. цифор: "))

rand(n)

rand(n2)

print()

print(n)
print(n2)

print()

matrix2 = []

for o in range(0, kolcif):

	n3 = []

	for i in range(0, kolcif):

		n3.append(int(n[o] * n2[i]))

	matrix2.append(n3)

printm(matrix2)

print()
print()

dey = input("Что вы хотите сделать с матрицами?\nДоступны: +, -, *, /: ")

if dey == "сложение":
	plusmat(matrix, matrix2)

elif dey == "вычитание":
	minusmat(matrix, matrix2)

elif dey == "умножение":
	umnmat(matrix, matrix2)

elif dey == "деление":
	delemat(matrix, matrix2)
