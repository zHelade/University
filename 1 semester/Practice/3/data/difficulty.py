def choose_difficulty(cur_hearts):
    if input(f'Хотите изменить сложность? (Сейчас: {cur_hearts} попыток) (y, если да): ') == 'y':
        print('\nВыберите сложность:\n1. Нормальная (5 попыток)\n2. Высокая (3 попытки)\n3. Luckyguy (1 попытка)')
        dif = {'1': 5, '2': 3, '3': 1}
        inp = str(input('Введите число от 1 до 3: '))
        while inp not in dif:
            print('Такого выбора вам не давали!')
            inp = str(input('Введите число от 1 до 3: '))
        print()
        return dif[inp]
    return cur_hearts


