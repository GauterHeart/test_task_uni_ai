import history
from random import randint
import os
import time


def generate_sequence(sequence):
    for i in range(500):
        sequence.append(randint(1,4))
    return sequence

def generate_score(score):
    score = randint(1,5)
    return score

if __name__ == '__main__':
    a = history.History()
    start_time = time.time()
    while True:
        if os.path.getsize('file.txt') >= 3221225472:
            print(f'Время на выполнение функции = {start_time}')
            print(f'Кол-во дубликвтов {a.score_dupl}')
            a.save_history('file.txt')
            a.load_history('file.txt')
            break
        sequence = []
        score = 0.0
        sequence = generate_sequence(sequence)
        score = generate_score(score)
        a.set_history(sequence, score)
    start_time_2 = time.time()
    while True:
        if os.path.getsize('file.txt') >= 5368709120:
            print(f'Время на выполнение функции = {start_time_2 + start_time}')
            print(f'Кол-во дубликвтов {a.score_dupl}')
            a.save_history('file.txt')
            a.load_history('file.txt')
            break
        sequence = []
        score = 0.0
        sequence = generate_sequence(sequence)
        score = generate_score(score)
        a.set_history(sequence, score)
