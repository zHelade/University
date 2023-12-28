def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        unique = set()
        for line in f:
            words = line.lower().split()
            words = [i.strip('.,!?;()[]-') for i in words]
            unique = unique.union(set(words))
    return list(unique)


def save_file(file_name, words):
    with open(file_name, 'w', encoding='utf-8') as f:
        head = f'Уникальных слов: {len(words)}\n{"="*20}\n'
        f.write(head)
        words.sort()
        for word in words:
            f.write(f'{word}\n')


if __name__ == '__main__':
    fn = 'data.txt'
    n_fn = 'count.txt'
    save_file(n_fn, read_file(fn))
