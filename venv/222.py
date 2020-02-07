from random import randint as rnd

a = (int(input("Введите длину списка №1: ")))
b = (int(input("Введите максимальное значение списка №1: ")))
c = (int(input("Введите длину списка №2: ")))
d = (int(input("Введите максимальное значение списка №2: ")))

def Good (a,b,c,d):
    list1 = []
    for i in range(a):
        list1.append(rnd(0, b))

    list2 = []
    for e in range(c):
        list2.append(rnd(0, d))

    list3 =[]

    for s in list1:
        if s in list2:
            list3.append(s)

    if len(list3) == 0:
        print ("Совпадений нет!!!")
        return list3
    else:
        return list(set(list3))

print (Good(a,b,c,d))

print("Good :D")