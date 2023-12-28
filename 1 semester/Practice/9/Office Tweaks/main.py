import os

import funcs
from funcs import create_interface, func_delete, func_change_dir, func_pdfdocx, func_cmp


c_dir = os.path.abspath(os.curdir)
while True:
    print(create_interface(c_dir))
    choice = input('Введите ваш выбор: ')
    match choice:
        case '1':
            c_dir = func_change_dir(c_dir)
            head = funcs.change_head(c_dir)
        case '2':
            # Преобразовать PDF в Docx
            func_pdfdocx('.pdf')
        case '3':
            # Преобразовать Docx в PDF
            func_pdfdocx('.docx')
        case '4':
            # Сжатие изображений
            func_cmp()
            continue
        case '5':
            # Удалить файлы
            func_delete(c_dir)
        case '0':
            # Выход
            break
