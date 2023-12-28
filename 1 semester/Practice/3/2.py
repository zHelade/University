import random as r


def win(word: list):
    print(' '.join(word))
    print('Поздравляем с победой!')


words = ['книга', 'месяц', 'ручка', 'шарик', 'олень', 'носок']
queue = r.sample(words, len(words))

for quest in queue:
    print('Мы начинаем игру поле чудес!')
    letters = list(quest.upper())
    h_letters = letters.copy()
    display = ['\u25A0' for x in range(len(quest))]
    hearts = 5

    while hearts != 0:
        print(f'{" ".join(display)}\t|\tПопыток: {hearts}')
        sug = str(input('Введите букву или слово: ')).upper()
        if len(sug) == 1:
            matches = letters.count(sug)
            if matches != 0:
                if sug not in display:
                    for i in range(matches):
                        ind = h_letters.index(sug)
                        display[ind] = sug
                        h_letters[ind] = None
                    if h_letters.count(None) == len(h_letters):
                        win(letters)
                        break
                else:
                    print('Эта буква уже была!')
            else:
                print('Такой буквы нет!')
                hearts -= 1
        else:
            if sug.upper() != quest.upper():
                print('Введите одну букву!')
                hearts -= 1
            else:
                win(letters)
                break

    else:
        print('Вы проиграли!')
        print(f'Ответ: {" ".join(letters)}')

    if quest != queue[-1]:
        while True:
            a = input('Хотите новое слово? (y/n): ')
            if a == 'y':
                break
            elif a == 'n':
                exit()
            else:
                print('Чего-чего?')
    else:
        print('А слова-то кончились!')