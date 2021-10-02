import random

zhestbota = int(random.randint(1,3))

youzhest = input("Камень, ножницы или бумага?: ")

if zhestbota == 1 and youzhest == "бумага":
        print("КАМЕНЬ\nты победил :(")

elif zhestbota == 1 and youzhest == "камень":
        print("КАМЕНЬ\nничья")

elif zhestbota == 1 and youzhest == "ножницы":
        print("КАМЕНЬ\nЯ победил!")

elif zhestbota == 2 and youzhest == "камень":
        print("НОЖНИЦЫ\nты победил :(")

elif zhestbota == 2 and youzhest == "ножницы":
        print("НОЖНИЦЫ\nничья")

elif zhestbota == 2 and youzhest == "бумага":
        print("НОЖНИЦЫ\nЯ победил!")

elif zhestbota == 3 and youzhest == "ножницы":
        print("БУМАГА\nты победил :(")

elif zhestbota == 3 and youzhest == "бумага":
        print("БУМАГА\nничья")

elif zhestbota == 3 and youzhest == "камень":
        print("БУМАГА\nЯ победил!")
