from random import randint as rnd

a = (int(input('Введите длину списка:')))
b = (int(input('Введите максимальное значение элемента списка: ')))

def Good (a,b):

    list = []

    for a in range(a):
        list.append(rnd(0,b))
    return list

print(Good(a,b))

print("Good :D")