import random as r


def format_time(t):
    if t < 10:
        t = '0'+str(t)
    return t


def generate_line(cites: list, events: list):
    num = r.randrange(1000)
    inout = r.choice(('прибыл из', 'отправился в'))
    city = r.choice(cites)
    h, m, s = r.randrange(24), r.randrange(59), r.randrange(60)
    m1 = m + 1
    h, m, m1, s = map(format_time, (h, m, m1, s))
    time1 = f'{h}:{m}:{s}'
    time2 = f'{h}:{m1}:{s}'
    event = r.choice(events)

    line = f'Рейс {num} {inout} {city} в {time1}\n' \
           f'Сообщение получено в {time2}\n{event}\n'
    return line


places = ['Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Казань', 'Нижний Новгород', 'Челябинск',
          'Омск', 'Самара', 'Ростов-на-Дону', 'Москва', 'Красноярск', 'Пермь', 'Воронеж']
junk = ['Случайная запись 1', 'Случайная запись 2', 'Запись случайная 3']
quantity = 10000

with open('journal.txt', 'w', encoding='utf-8') as f:
    for i in range(quantity):
        log = generate_line(places, junk)
        f.write(log)
