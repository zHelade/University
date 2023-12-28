def get_new_log(log):
    line = log.rstrip().split()

    num = line[1]
    inout = line[3]
    time_id = len(line)-1
    time = line[time_id]
    city = ' '.join(line[4:time_id-1])

    return f'[{time}] - Поезд № {num} {inout} {city}\n'


log_fn = 'journal.txt'
new_log_fn = 'log.txt'
with open(log_fn, 'r', encoding='utf-8') as j:
    with open(new_log_fn, 'w', encoding='utf-8') as nl:
        for log in j:
            if 'Рейс' in log:
                nl.write(get_new_log(log))
