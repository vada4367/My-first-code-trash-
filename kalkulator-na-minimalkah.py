#!/usr/bin/python
print("калькулятор\n")

#переменная отвечающая за кол действий
what2 = input("сколько будет действий? (максимум 2):")

#если одно или два действия то будет вопрос для переменной какое первое число
if what2 == "1" or "2":
    a = input("\nкакое первое число?:")
    a = float(a)

#если одно действие то
if what2 == "1":

#сначало запрос на переменную отвечающую за действие
    what = input("\nкакое действие сделаете?\nдоступны: деление умножение сложение вычитание\n")

#потом запрос на переменную второго числа
    b = input("\nкакое второе число?:")
    b = float(b)

# в зависимости от переменной what зависит действие
    if what == "сложение":
        c = a + b
        print("\nответ: " + str(c)) 
     
    elif what == "вычитание":
        c = a - b
        print("\nответ: " + str(c)) 
     
    elif what == "умножение":
        c = a * b
        print("\nответ: " + str(c)) 
     
    elif what == "деление":
        c = a / b
        print("\nответ: " + str(c)) 

#ошибка
    else:
        print("ты неправильно написал(а) действие)") 

#если два действия то
elif what2 == "2":

#какое первое действие
    what = input("\nкакое действие сделаете?\nдоступны: деление умножение сложение вычитание\n")

#какое второе число
    b = input("\nкакое второе число?:")
    b = float(b)

# в зависимости от переменной what зависит действие
    if what == "сложение":
        d = a + b
        d = float(d)
        
    elif what == "вычитание":
        d = a - b
        d = float(d)
        
    elif what == "умножение":
        d = a * b
        d = float(d)
              
    elif what == "деление":
        d = a / b
        d = float(d)

#запрос на переменную what3 означающая второе действие
    what3 = input("\nкакое второе действие сделаете?\n")

#какое третье число
    c = input("\nкакое третье число?:")
    c = float(c)

# в зависимости от переменной what3 зависит второе действие 
    if what3 == "сложение":
        e = d + c
        print("\nответ: " + str(e))

    elif what3 == "вычитание":
        e = d - c
        print("\nответ: " + str(e))
    
    elif what3 ==  "умножение":
        e = d * c
        print("\nответ: " + str(e))
              
    elif what3 == "деление":
        e = d / c
        print("\nответ: " + str(e))

#ошибка
    else:
            print("ты неправильно написал(а) действие)")

#серьёзная ошибка
else:
    print("хз какая-то неизвестная ошибка")
