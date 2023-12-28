import os.path


def get_record():
    path = 'data/records.txt'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return int(f.readline())
    with open(path, 'w', encoding='utf-8') as f:
        f.write('0')
        return 0


def save_record(score: int, record: int):
    if score > record:
        print('Вы поставили новый рекорд!')
        path = 'data/records.txt'
        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(score))
