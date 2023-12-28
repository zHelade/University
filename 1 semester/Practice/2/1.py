import random as r
# 28*12 = 336

iters = 100000

c = 0
num = 23
for i in range(iters):
    birthdays = [r.randrange(336) for x in range(num)]
    for man in birthdays:
        if birthdays.count(man) > 1:
            c += 1
            break

print(f'В группе из 23 человек шанс равен: {round(c/iters*100, 1)}%')

c = 0
num = 60
for i in range(iters):
    birthdays = [r.randrange(336) for x in range(num)]
    for man in birthdays:
        if birthdays.count(man) > 1:
            c += 1
            break

print(f'В группе из 60 человек шанс равен: {round(c/iters*100, 1)}%')
