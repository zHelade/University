import random as r
# 28*12 = 336


def birthday(iters):
    c = 0
    num = 23
    for i in range(iters):
        birthdays = [r.randrange(336) for x in range(num)]
        for man in birthdays:
            if birthdays.count(man) > 1:
                c += 1
                break
    return c/iters*100


iters = int(input('Введите кол-во итераций: '))
print(f'В группе из 23 человек шанс равен: {round(birthday(iters), 1)}%')
