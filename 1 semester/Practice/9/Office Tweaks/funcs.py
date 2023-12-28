import os
import pdf2docx
from docx2pdf import convert
from PIL import Image


# Интерфейс
def change_head(directory: str) -> str:
    new_head = (f'Текущий каталог: {directory}\n\n'
                f'Выберите действие:\n\n')
    return new_head


def create_interface(current_directory: str) -> str:
    """Создание консольного интерфейса"""
    main_menu = ('1. Сменить рабочий каталог\n'
                 '2. Преобразовать PDF в Docx\n'
                 '3. Преобразовать Docx в PDF\n'
                 '4. Произвести сжатие изображений\n'
                 '5. Удалить группу файлов\n'
                 '0. Выход\n')
    return change_head(current_directory) + main_menu


# Первая функция
def change_dir(path: str) -> bool:
    """Смена рабочего каталога"""
    if os.path.exists(path):
        os.chdir(path)
        return True
    return False


def func_change_dir(cur_directory: str) -> str:
    # Сменить директорию
    user_path = input('Укажите путь к каталогу:\n')
    if change_dir(user_path):
        new_path = user_path
        return new_path
    print('Такой директории не существует, или путь введен не верно\n')
    return cur_directory


# Вторая функция и третья функции
def choose_files(ex: str) -> list:
    """Возврат списка файлов с требуемым расширением"""
    files = [f for f in os.listdir(path='.') if f.endswith(ex)]
    return files


def sub_interface(ex: str, files: list) -> bool:
    """Возврат при наличии файлов с требуемым расширением True|False"""
    if len(files) != 0:
        print(f'\nСписок файлов с расширением {ex}:')
        for i in range(len(files)):
            print(f'{i+1}. {files[i]}')
        return True
    print(f'Файлов с расширением {ex} нет в директории')
    return False


def do_pdf2docx(file: str):
    """Создание файлов docx расширения"""
    file_docx = file.replace('.pdf', '.docx')
    pdf2docx.parse(file, file_docx)


def do_docx2pdf(file: str):
    file_pdf = file.replace('.docx', '.pdf')
    print(file, file_pdf)
    convert(file)


def get_files_index(user_input: str) -> list:
    user_input = user_input.replace(' ', '')
    return user_input.split(',')


def func_pdfdocx(file_type: str):
    if file_type == '.pdf':
        change_func = do_pdf2docx
    else:
        change_func = do_docx2pdf

    files = choose_files(file_type)
    if sub_interface(file_type, files):
        print('Введите номер файлов (1), диапазон номеров (1-100) или список файлов (1,12,23)\n'
              'Если хотите преобразовать все файлы введите -1. Для возврата введите 0')
        choice = input('Ваш выбор: ')
        if choice == '0':
            return
        elif choice == '-1':
            for file in files:
                change_func(file)
        else:
            indexes = get_files_index(choice)
            for i in indexes:
                if '-' not in i:
                    file = files[int(i)-1]
                    change_func(file)
                else:
                    ranges = tuple(map(int, i.split('-')))
                    for k in range(ranges[0], ranges[1]):
                        file = files[int(k)]
                        change_func(file)
    return


# Пятая функция
def del_choice(choice: str) -> list:
    """Возврат подходящих файлов под критерий"""
    substr = input('Введите подстроку: ')
    all_files = [f for f in os.listdir(path='.')]
    files_to_del = []
    match choice:
        case '1':
            files_to_del = [f for f in all_files if f.startswith(substr)]
        case '2':
            files_to_del = [f for f in all_files if f.endswith(substr)]
        case '3':
            files_to_del = [f for f in all_files if substr in f]
        case '4':
            files_to_del = [f for f in all_files if f.endswith('.' + substr)]
    return files_to_del


# Удалить подходящие файлы
def del_files(directory: str, files: list):
    """Удаление файлов из списка"""
    if len(files) != 0:
        for file in files:
            os.remove(f'{directory}\\{file}')


# Функция выборочного удаления
def func_delete(directory: str):
    del_menu = ('Действия:\n'
                '0. Вернуться назад\n'
                '1. Удалить все файлы начинающиеся на определенную подстроку\n'
                '2. Удалить все файлы заканчивающиеся на определенную подстроку\n'
                '3. Удалить все файлы содержащие определенную подстроку\n'
                '4. Удалить все файлы по расширению\n')
    print(del_menu)
    choice = input('Введите ваш выбор: ')
    files_to_del = del_choice(choice)
    del_files(directory, files_to_del)
    print(f'Удалено {len(files_to_del)} файлов')


# Четвертая функция
def compress_img(file: str, cmp_rate: int) -> None:
    try:
        with Image.open(file) as im:
            im.save(f'cmp_{file}', quality=cmp_rate)
    except OSError:
        print("Невозможно сжать", file)


def func_cmp():
    exs = '.jpeg', '.jpg', '.gif', '.png'
    files = []
    for ex in exs:
        files += choose_files(ex)
    if sub_interface(str(exs), files):
        print('Введите номер файлов (1), диапазон номеров (1-100) или список файлов (1,12,23)\n'
              'Если хотите преобразовать все файлы введите -1. Для возврата введите 0')
        choice = input('Ваш выбор: ')
        cmp_rate = int(input('Введите степень сжатия (0-100): '))
        if choice == '0':
            return
        elif choice == '-1':
            for file in files:
                compress_img(file, cmp_rate)
        else:
            indexes = get_files_index(choice)
            for i in indexes:
                if '-' not in i:
                    file = files[int(i) - 1]
                    compress_img(file, cmp_rate)
                else:
                    ranges = tuple(map(int, i.split('-')))
                    for k in range(ranges[0], ranges[1]):
                        file = files[int(k)]
                        compress_img(file, cmp_rate)
    return
