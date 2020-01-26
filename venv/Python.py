from random import  randrange as rnd
a = rnd(0,10)
b = rnd(0,10)
c = rnd(0,10)
if a > b:
    print('Хорошо')
elif a < b:
    print('Плохо')
elif a == b:
    print(b,'Теперь эта!')
    print(b,a + b)
    if (a + b) < b:
        print('Отлично')
    elif (a + b) > b:
        print('Ужасно')
    elif (a + b) == b:
        print('О УЖАС')


