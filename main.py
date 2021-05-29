ExitCode = 1
# Код выхода

while ExitCode != "0":
    
    # Блок импорта  модулей
    import array
    # from array import*
    from random import shuffle
    from random import choice
    # from random import *
    import operator
    import tkinter as tk
    import os
    import ctypes
    from ctypes import windll
    # from ctypes import *
    import re

    # Блок ввода из файла
    f = open("Asks.txt", "r", encoding='utf-8')
    Quests = ['q']*90
    for i in range(0, 90):
        Quests[i] = f.readline()
        
    f.close()
    KeyAnswers = ['q']*90
    k = open("Anses.txt", "r", encoding="utf-8")
    for i in range(0, 90):
        KeyAnswers[i] = k.readline()
    k.close()

    # Установка оптимального интерфейса
    x = (windll.user32.GetSystemMetrics(0))//8
    y = (windll.user32.GetSystemMetrics(1))//8
    os.system('mode con cols=' + str(x) + ' lines=' + str(y))
    os.system('color 2f')

    class Gamer:
        """Создание класса Игрок """
        def __init__(self, name, points):
            self.name = name
            self.points = points


    # Блок функций:

    # Блок функций графического окна


    def write(a):

        """Вывод в графическое окно """

        label = tk.Label(
            text=a,
            font="Times 15",
            fg="blue",
            bg="pink",

            width=240,

            height=30,
        )
        label.pack()


    def open_up():
        """Открытие графического окна """
        window = tk.Tk()  
        window.title("Поле чудес")  
        window.geometry('3900x2500')
        window.configure(background='pink')
        return window


    def winner_congrats(a, b):
        """Блок объявления победителя в графическом окне """
        c = a+b
        label = tk.Label(
            text=c,
            font="Times 15",
            fg="blue",
            bg="pink",
            width=240,
            height=30,
        )
        label.pack()

    def random_drum(players_list):
        """Формирование порядка ходов между игроками """
        shuffle(players_list)
        return players_list


    def random_drum_case():
        """Функция "барабан", определяющая событие в игре"""
        cases = [250, 500, 750, 800]*4+[0]+[2]
        game_case = choice(cases)
        print(game_case, ' На барабане')
        return game_case


    def score_count(score, action):
        """Функция подсчета баллов """
        if action == 2:
            score = score*2
        else:
            score = score+action
        return score
      

    def second_chance():
        """Функция второго шанса """
        chance_case = [0, 0, 0, 0, 1]
        second_chance_turn = choice(chance_case)
        return second_chance_turn

    # Блок открытия приветственного окна
    win = open_up()
    Btn = tk.Button(text="Начать игру!", command=win.destroy, padx="20", pady="8", fg="red", bg="yellow",)
    
    write("Добро пожаловать на Поле Чудес!")
    Btn.pack()
    win.mainloop()

    # Ввод номера игры
    print("Введите номер игры от 1 до 30!")
    NumberOfGame = int(input())
    
    while NumberOfGame < 1 or NumberOfGame > 30:
        print("Ошибка! Необходимо ввести ЧИСЛО от 1 до 30!")
        NumberOfGame = int(input())

    # Блок первоначальных переменных из файла
    Question1 = Quests[NumberOfGame*3-3]
    
    Answer11 = KeyAnswers[NumberOfGame*3-3]
    Answer11 = Answer11[0:-1]
    
    Answer1 = []
    for letter in Answer11:
        Answer1.append(letter)

    Answer1Hidden = ["*"]*len(Answer1)

    Question2 = Quests[NumberOfGame*3-2]
    Answer22 = KeyAnswers[NumberOfGame*3-2]
    Answer22 = Answer22[0:-1]
    Answer2 = []
    for letter in Answer22:
        Answer2.append(letter)
       
    Answer2Hidden = ["*"]*len(Answer2)
        
    Question3 = Quests[NumberOfGame*3-1]
    Answer33 = KeyAnswers[NumberOfGame*3-1]
    Answer3 = []
    Answer33 = Answer33[0:-1]
    for letter in Answer33:
        Answer3.append(letter)
      
    Answer3Hidden = ["*"]*len(Answer3)
    
    Questions = [Question1, Question2, Question3]
    Answers = [Answer11, Answer22, Answer33]
    AnswersInList = [Answer1, Answer2, Answer3]
    AnswersHidden = [Answer1Hidden, Answer2Hidden, Answer3Hidden]

    # Блок ввода количества игроков

    print("Введите количество игроков:от 2 до 6!")
    NumberOfPlayers = str(input())
    while NumberOfPlayers.isdigit is False or NumberOfPlayers < "2" or NumberOfPlayers > "6":
        print("Ошибка! Необходимо ввести ЧИСЛО от 2 до 6!")
        NumberOfPlayers = str(input())
         
    NumberOfPlayers = int(NumberOfPlayers)

    # Блок ввода никнеймов игроков
    print("Введите Ваши никнеймы!")
    PlayersInfo = [Gamer]*NumberOfPlayers
    for i in range(NumberOfPlayers):
        print("Введите никнейм игрока номер", i+1, ":")
        arg = str(input())
        PlayersInfo[i] = Gamer(arg, 0)

    # Инициализация раундов
    for RoundNumber in range(3):
        
        flag = 0
        SolutionInList = AnswersInList[RoundNumber]
        Solution = Answers[RoundNumber]
        SolutionHidden = AnswersHidden[RoundNumber]
        AvoidRepeat = []*len(SolutionInList)
        flag = 0
        print("Раунд ", RoundNumber+1)
        print("Ответ записывается заглавными буквами!")
        print("За слово, отгаданное целиком дается 2000 баллов")
        print("При выпадении '0' на барабане ваши баллы обнуляются")
        print("При выпадении '2' на барабане ваши очки удваиваются!")
        PlayersInfo = random_drum(PlayersInfo)
        print("Порядок хода:")
        for i in range(NumberOfPlayers):
            print(PlayersInfo[i].name)
        print("Вопрос: ", Questions[RoundNumber])
        print("Слово-ответ", SolutionHidden)

        # Угадывание буквы или слова
        while SolutionInList != SolutionHidden:
            for i in range(NumberOfPlayers):
                turn = 0
              
                while turn == 0 and flag == 0:
                    Fate = random_drum_case()
                    if Fate == 0:
                        PlayersInfo[i].points = 0
                    print("Ходит ", PlayersInfo[i].name)
                    guess = str(input())
                    # Избежание повтора
                    if guess in AvoidRepeat:
                        print("Эту букву уже открыли! Ход передается другому игроку!")
                        turn = 1
                    # Буква отгадана
                    elif guess in SolutionInList:
                        AvoidRepeat.append(guess)
                        print("Верно! Такая буква есть в слове!")
                        PlayersInfo[i].points = score_count(PlayersInfo[i].points, Fate)
                        print(PlayersInfo[i].name, " имеет количество баллов ", PlayersInfo[i].points)
                        for j in range(len(SolutionInList)):
                            if SolutionInList[j] == guess:
                               SolutionHidden[j] = guess
                        print("Слово-ответ", SolutionHidden)
                        if SolutionInList == SolutionHidden:
                            flag = 1
                      
                    # слово отгадано
                    elif guess == Solution:
                        print("Вы угадали слово!")
                        PlayersInfo[i].points = PlayersInfo[i].points+2000
                        print(PlayersInfo[i].name, " имеет количество баллов ", PlayersInfo[i].points)
                        print("Ответ: ", SolutionInList)
                        SolutionHidden = SolutionInList
                        flag = 1
                    # ошибка и второй шанс
                    elif second_chance() == 1:
                        print("Вы ошиблись, но вам выпал второй шанс!")
                    else:
                        print("Вы ошиблись! Ход передается следующему игроку!")
                        turn = 1

            for k in range(NumberOfPlayers):
                print(PlayersInfo[k].name, " набрал ", PlayersInfo[k].points)

            print("                        ")

    # Подведение итогов
    PlayersInfo = sorted(PlayersInfo, key=operator.attrgetter('points'))
    for i in range(NumberOfPlayers):
        print(PlayersInfo[i].name,  " занял ", NumberOfPlayers-i, " место и набрал баллов: ",  PlayersInfo[i].points)
    win = open_up()
    Btn = tk.Button(text="Продолжить", command=win.destroy, padx="20", pady="8", fg="red", bg="yellow",)
    
    winner_congrats("ПОБЕДИТЕЛЬ:   ", PlayersInfo[NumberOfPlayers - 1].name)
    Btn.pack()
    win.mainloop()

    # Блок выхода или продолжения
    print("Введите 0 для выхода или любой символ для продолжения!")
    ExitCode = str(input())
