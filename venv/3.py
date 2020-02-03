from random import randint as rnd

a = rnd(0, 999)
t = dict.fromkeys([str(input('Введите слово'))], a)

print(t)
