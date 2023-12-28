import random as r


def monty_hall(iters):
    c_false = 0
    c_true = 0
    prize = 0

    for i in range(iters):
        chosen_one = r.randrange(3)
        if chosen_one == prize:
            c_false += 1

    for j in range(iters):
        chosen_one = r.randrange(2)
        if chosen_one == 0:
            c_true += 1
    return c_false/c_true*100


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
