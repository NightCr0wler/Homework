from random import  randrange as rnd

list = []

for a in range(10):
    list.append(rnd(0,99))

print(list)

del list[-1]
print(list)