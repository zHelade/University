file_n = str(input('Введите имя файла: '))
a = []
try:
    f = open(file_n, 'r', encoding='utf-8')     # файла нет
except FileNotFoundError:
    print('Такого файла не существует!')
else:
    try:
        n = int(f.readline())    # нельзя перевести в инт
    except ValueError:
        print('Файл должен содержать только числа!')
    else:
        try:
            for i in range(n):      # вне области n
                a.append(int(f.readline()))     # нельзя перевести в инт
        except ValueError:
            print('Файл содержит некорректные данные!')
        except KeyboardInterrupt:
            print('Операция прервана!')
        else:
            print(a)
    finally:
        f.close()
