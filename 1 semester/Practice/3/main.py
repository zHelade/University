from data import words, records, difficulty


def win(word: list):
    print(' '.join(word))
    print('Поздравляем с победой!')
    return 1


if __name__ == '__main__':
    queue = words.get_words()
    score = 0

    for quest in queue:
        print('Мы начинаем новую игру!')
        record = records.get_record()
        print(f'Текущий счет: {score}\t|\tВаш рекорд: {record}')
        letters = list(quest.upper())
        h_letters = letters.copy()
        display = ['\u25A0' for x in range(len(quest))]
        hearts = difficulty.choose_difficulty(5)

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
                            score += win(letters)
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
                    score += win(letters)
                    break

        else:
            print('Вы проиграли!')
            print(f'Ответ: {" ".join(letters)}')

        if quest != queue[-1]:
            while True:
                a = input('\nХотите новое слово? (y/n): ')
                if a == 'y':
                    break
                elif a == 'n':
                    print('Ваш счет равен', score)
                    records.save_record(score, record)
                    exit()
                else:
                    print('Чего-чего?')
        else:
            print('А слова-то кончились!')
