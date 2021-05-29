# Функции для работы случайных событий
from random import shuffle
from random import choice

def random_drum(players_list):
    """Формирование порядка ходов между игроками """
    shuffle(players_list)
    return players_list

def random_drum_case():
    """Функция "барабан", определяющая событие в игре"""
    cases = [250, 500, 750, 800] * 4 + [0] + [2]
    game_case = choice(cases)
    print(game_case, ' На барабане')
    return game_case

def score_count(score, action):
    """Функция подсчета баллов """
    if action == 2:
        score = score * 2
    else:
        score = score + action
    return score

def second_chance():
    """Функция второго шанса """
    chance_case = [0, 0, 0, 0, 1]
    second_chance_turn = choice(chance_case)
    return second_chance_turn