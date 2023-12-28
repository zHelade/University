import pymorphy3
import re
from translate import Translator


def sort_dict(dictionary: dict) -> dict:
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    sorted_dictionary = {key: value for key, value in sorted_items}
    return sorted_dictionary


pattern = '[а-яА-ЯёЁ]+'
morph = pymorphy3.MorphAnalyzer()

f_name = 'dialouge.txt'
f_name_nf = f_name.replace('.txt', '_normal_form.txt')
count_w = {}

with open(f_name_nf, encoding='utf-8', mode='w') as out_f:
    with open(f_name, encoding='utf-8', mode='r') as in_f:
        for line in in_f:
            if '>' not in line:
                msg = re.findall(pattern, line)
                for word in msg:
                    n_f = morph.parse(word)[0].normal_form
                    if count_w.get(n_f) is None:
                        count_w[n_f] = 1
                    else:
                        count_w[n_f] = count_w[n_f] + 1
                    out_f.write(n_f + '\n')


with open('output.txt', encoding='utf-8', mode='w') as out_f:
    ru_dict = sort_dict(count_w)
    en_dict = {}
    translator = Translator(to_lang='en', from_lang='ru', provider='mymemory')
    items = ru_dict.items()

    print('starting translation')
    for key, value in items:  # translated_dict = {translator.translate(key): value for key, value in items}
        e_word = translator.translate(key)
        en_dict[e_word] = value
        string = f'{key} | {e_word} | {value}\n'
        out_f.write(string)
    print('done')
