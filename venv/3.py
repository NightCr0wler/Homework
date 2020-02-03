from random import randint as rnd

a = rnd(0, 999)
t = dict.fromkeys([str(input("Введіть будь-яку фразу та натисніть Enter: "))], a)

print(t)
