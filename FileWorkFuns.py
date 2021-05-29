# Массивы для ответов и вопросов
Quests = ['q'] * 90
KeyAnswers = ['q'] * 90


# Блок ввода из файла


class AnsAndQuests:
    """Ответы и вопросы, распарсенные в буквы"""
    questions = ["q"] * 3
    answers = ["q"] * 3
    answers_hidden = ["q"] * 3
    answers_in_list = ["q"] * 3

    def __init__(self):
        pass


AnsAndQuestsClass = AnsAndQuests()


def input_from_file():
    """Ввод всего содержимого из файла в переменные"""
    f = open("Asks.txt", "r", encoding='utf-8')

    for i in range(0, 90):
        Quests[i] = f.readline()

    f.close()

    k = open("Anses.txt", "r", encoding="utf-8")
    for i in range(0, 90):
        KeyAnswers[i] = k.readline()
    k.close()


def copy_data(game_number):
    """Выбор вопросов и ответов для раунда и распарсивание по буквам"""

    question1 = Quests[game_number * 3 - 3]

    answer11 = KeyAnswers[game_number * 3 - 3]
    answer11 = answer11[0:-1]

    answer1 = []
    for letter in answer11:
        answer1.append(letter)

    answer1_hidden = ["*"] * len(answer1)

    question2 = Quests[game_number * 3 - 2]
    answer22 = KeyAnswers[game_number * 3 - 2]
    answer22 = answer22[0:-1]
    answer2 = []
    for letter in answer22:
        answer2.append(letter)

    answer2_hidden = ["*"] * len(answer2)

    question3 = Quests[game_number * 3 - 1]
    answer33 = KeyAnswers[game_number * 3 - 1]
    answer3 = []
    answer33 = answer33[0:-1]
    for letter in answer33:
        answer3.append(letter)

    answer3_hidden = ["*"] * len(answer3)

    AnsAndQuests.questions = [question1, question2, question3]
    AnsAndQuests.answers = [answer11, answer22, answer33]
    AnsAndQuests.answers_in_list = [answer1, answer2, answer3]
    AnsAndQuests.answers_hidden = [answer1_hidden, answer2_hidden, answer3_hidden]
