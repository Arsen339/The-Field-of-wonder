# Блок импорта  модулей(встроеных)
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

# импорт из созданных модулей
from GraphicWindowFuns import *
from RandomFuns import *
from MistakeProtectFuns import *
from FileWorkFuns import *

# Код выхода
ExitCode = 1


while ExitCode != "0":

    input_from_file()

    class Gamer:
        """Создание класса Игрок """
        def __init__(self, name, points):
            self.name = name
            self.points = points


    # Блок функций:

    # Блок функций графического окна
    make_window()
    make_ui()

    # Ввод номера игры с проверкой
    print("Введите номер игры от 1 до 30!")
    NumberOfGame = str(input())
    if defend_game_number(NumberOfGame) == 0:
        continue
    NumberOfGame = int(NumberOfGame)

    # Блок первоначальных переменных из файла
    copy_data(NumberOfGame)

    # Блок ввода количества игроков с проверкой
    print("Введите количество игроков:от 2 до 6!")
    NumberOfPlayers = str(input())
    if defend_gamer_number(NumberOfPlayers) ==0:
        continue
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
        SolutionInList = AnsAndQuestsClass.answers_in_list[RoundNumber]
        Solution = AnsAndQuestsClass.answers[RoundNumber]
        SolutionHidden = AnsAndQuestsClass.answers_hidden[RoundNumber]
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
        print("Вопрос: ", AnsAndQuestsClass.questions[RoundNumber])
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
                    guess = guess.upper()
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
