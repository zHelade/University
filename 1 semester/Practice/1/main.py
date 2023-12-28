from random import randrange

prize = 0   # Дверь 0 - всегда победная
# c_false - не принял предложение ведущего, с_true - принял
c_false = 0
c_true = 0
iterations = 100000
'''
Если изначально выбрал нужную дверь, то при принятии предложения ведущего проиграет.
Номер выйгрышной двери не важен, как и выбранной неверно.

Изначально шанс победить равен 33%, но после открытия двери ведущим выбор становиться из двух дверей, шанс победы
равен 50%, если принял предложение, что на ~60% больше чем 33%.
'''

# Не принимал предложения ведущего
for i in range(iterations):
    chosen_one = randrange(3)
    if chosen_one == prize:
        c_false += 1

# Принимал предложения ведущего
for j in range(iterations):
    # Что бы в первый раз игрок не выбрал, при принятии предложеения ведущего, выбор состоит из двух дверей
    chosen_one = randrange(2)
    if chosen_one == 0:
        c_true += 1

print(f'Не принял и победил: {c_false} из 100000. {round(c_false/iterations*100, 2)}%')
print(f'Принял и победил: {c_true} из 100000. {round(c_true/iterations*100, 2)}%')
print(f'Разница в шансах: {round(c_false/c_true*100, 2)}%')

