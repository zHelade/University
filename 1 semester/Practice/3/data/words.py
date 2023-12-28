import random as r


def get_words():
    with open('data/words.txt', 'r', encoding='utf-8') as f:
        words = []
        for line in f:
            words.append(line.rstrip())
    return r.sample(words, len(words))
