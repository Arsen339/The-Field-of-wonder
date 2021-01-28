ExitCode=1
#Код выхода
while ExitCode !="0":
    
    #Блок импорта  модулей
    import array
    #from array import*
    from random import shuffle
    from random import choice
    #from random import *
    import operator
    import tkinter as tk
    import os
    import ctypes
    from ctypes import windll
    #from ctypes import *
    import re

    #Блок ввода из файла
    f=open("Asks.txt","r", encoding='utf-8')
    Quests=['q']*90
    for i in range(0,90):
        Quests[i]=f.readline()
        
    f.close()
    KeyAnswers=['q']*90
    k=open("Anses.txt","r",encoding="utf-8")
    for i in range(0,90):
        KeyAnswers[i]=k.readline()
    k.close()


    
    #Установка оптимального интерфейса
    x = (windll.user32.GetSystemMetrics(0))//8
    y = (windll.user32.GetSystemMetrics(1))//8
    os.system('mode con cols=' + str(x)+ ' lines=' + str(y))
    os.system('color 2f')
    

    #Создание класса Игрок
    class Gamer:
        def __init__(self, Name, Points):
            self.Name=Name
            self.Points=Points


    #Блок функций:

    #Блок функций графического окна

    #Вывод в графическое окно
    def write(a):
        label = tk.Label(
        text=a,
        font="Times 15",
        fg="blue",
        bg="pink",
        width=240,
        height=30,
        )
        label.pack()

    #Открытие графического окна
    def OpenUp():
        window = tk.Tk()  
        window.title("Поле чудес")  
        window.geometry('3900x2500')
        window.configure(background='pink')
        return window

    #Блок объявления победителя в графическом окне
    def WinnerCongrats(a,b):
        c=a+b
        label = tk.Label(
        text=c,
        font="Times 15",
        fg="blue",
        bg="pink",
        width=240,
        height=30,
        )
        label.pack()



        #Формирование порядка ходов между игроками
    def RandomDrum(PlayersList):
        shuffle(PlayersList)
        return PlayersList

    #Функция "барабан", определяющая событие в игре
    def RandomDrumCase():  
      Cases=[250, 500, 750, 800]*4+[0]+[2]
      GameCase=choice(Cases)
      print(GameCase,' На барабане')
      return GameCase

    #Функция подсчета баллов
    def ScoreCount(score, action):
        if action==2:
            score=score*2
        else:
            score=score+action
        return score
      
    #Функция второго шанса
    def SecondChance():
      ChanceCase=[0,0,0,0,1]
      SecondChanceTurn=choice(ChanceCase)
      return SecondChanceTurn

    #Блок открытия приветственного окна
    win=OpenUp()
    Btn=tk.Button(text="Начать игру!", command=win.destroy, padx="20", pady="8",fg="red",
    bg="yellow",)
    
    write("Добро пожаловать на Поле Чудес!")
    Btn.pack()
    win.mainloop()


    #ввод номера игры
    print("Введите номер игры от 1 до 30!")
    NumberOfGame=int(input())
    
    while  NumberOfGame<1 or NumberOfGame >30:
        print("Ошибка! Необходимо ввести ЧИСЛО от 1 до 30!")
        NumberOfGame=int(input())

    
        
         
    

    #Блок первоначальных переменных из файла
    Question1=Quests[NumberOfGame*3-3]
    
    Answer11=KeyAnswers[NumberOfGame*3-3]
    Answer11=Answer11[0:-1]
    
    Answer1=[]
    for letter in Answer11:
        Answer1.append(letter)
    
    
    Answer1Hidden=["*"]*len(Answer1)

    Question2=Quests[NumberOfGame*3-2]
    Answer22=KeyAnswers[NumberOfGame*3-2]
    Answer22=Answer22[0:-1]
    Answer2=[]
    for letter in Answer22:
        Answer2.append(letter)
       
    Answer2Hidden=["*"]*len(Answer2)
        
    Question3=Quests[NumberOfGame*3-1]
    Answer33=KeyAnswers[NumberOfGame*3-1]
    Answer3=[]
    Answer33=Answer33[0:-1]
    for letter in Answer33:
        Answer3.append(letter)
      
    Answer3Hidden=["*"]*len(Answer3)
    
    Questions=[Question1, Question2, Question3]
    Answers=[Answer11, Answer22, Answer33]
    AnswersInList=[Answer1, Answer2, Answer3]
    AnswersHidden=[Answer1Hidden, Answer2Hidden, Answer3Hidden]







    


    
    #Блок ввода количества игроков
    print("Введите количество игроков:от 2 до 6!")
    NumberOfPlayers=str(input())
    while NumberOfPlayers.isdigit == False or NumberOfPlayers<"2" or NumberOfPlayers >"6":
        print("Ошибка! Необходимо ввести ЧИСЛО от 2 до 6!")
        NumberOfPlayers=str(input())
         
    NumberOfPlayers=int(NumberOfPlayers)



    #Блок ввода никнеймов игроков
    print("Введите Ваши никнеймы!")
    PlayersInfo=[Gamer]*NumberOfPlayers
    for i in range(NumberOfPlayers):
      print("Введите никнейм игрока номер", i+1, ":")
      arg=str(input())
      PlayersInfo[i]=Gamer(arg,0)




    #Инициализация раундов
    for RoundNumber in range(3):
        
        flag=0
        SolutionInList=AnswersInList[RoundNumber]
        Solution=Answers[RoundNumber]
        SolutionHidden=AnswersHidden[RoundNumber]
        AvoidRepeat=[]*len(SolutionInList)
        flag=0
        print("Раунд ", RoundNumber+1)
        print("Ответ записывается заглавными буквами!")
        print("За слово, отгаданное целиком дается 2000 баллов")
        print("При выпадении '0' на барабане ваши баллы обнуляются")
        print("При выпадении '2' на барабане ваши очки удваиваются!")
        PlayersInfo=RandomDrum(PlayersInfo)
        print("Порядок хода:")
        for i in range(NumberOfPlayers):
            print(PlayersInfo[i].Name)
        print("Вопрос: ", Questions[RoundNumber])
        print("Слово-ответ", SolutionHidden)

        #угадывание буквы или слова
        while SolutionInList != SolutionHidden:
            for i in range(NumberOfPlayers):
              turn=0
              
              while turn==0 and flag==0:
                  Fate=RandomDrumCase()
                  if Fate==0:
                      PlayersInfo[i].Points=0
                  print("Ходит ",PlayersInfo[i].Name)
                  guess=str(input())
                  #избежание повтора
                  if guess in AvoidRepeat: 
                      print("Эту букву уже открыли! Ход передается другому игроку! В следующий раз будьте внимательней!")
                      turn=1
                  #буква отгадана
                  elif guess in SolutionInList:
                      AvoidRepeat.append(guess)
                      print("Верно! Такая буква есть в слове!")
                      PlayersInfo[i].Points=ScoreCount(PlayersInfo[i].Points,Fate)
                      print(PlayersInfo[i].Name , " имеет количество баллов ", PlayersInfo[i].Points)
                      for j in range(len(SolutionInList)):
                          if SolutionInList[j]==guess:
                             SolutionHidden[j]=guess
                      print("Слово-ответ", SolutionHidden)
                      if SolutionInList == SolutionHidden:
                          flag=1
                      
                  #слово отгадано  
                  elif guess==Solution:
                    print("Вы угадали слово!")
                    PlayersInfo[i].Points=PlayersInfo[i].Points+2000
                    print(PlayersInfo[i].Name," имеет количество баллов ", PlayersInfo[i].Points)
                    print("Ответ: ", SolutionInList)
                    SolutionHidden=SolutionInList
                    flag=1
                  #ошибка и второй шанс 
                  elif SecondChance()==1:
                    print("Вы ошиблись, но вам выпал второй шанс!")
                  else:
                      print("Вы ошиблись! Ход передается следующему игроку!")
                      turn=1


        for k in range(NumberOfPlayers):
            print(PlayersInfo[k].Name, " набрал ", PlayersInfo[k].Points)
     

        print("                        ")

    #Подведение итогов
    PlayersInfo=sorted(PlayersInfo, key=operator.attrgetter('Points'))
    for i in range(NumberOfPlayers):
        print(PlayersInfo[i].Name,  " занял ",NumberOfPlayers-i, " место и набрал баллов: ",  PlayersInfo[i].Points)
    win=OpenUp()
    Btn=tk.Button(text="Продолжить", command=win.destroy, padx="20", pady="8",fg="red",
    bg="yellow",)
    
    WinnerCongrats ("ПОБЕДИТЕЛЬ:   ",PlayersInfo[NumberOfPlayers-1].Name)
    Btn.pack()
    win.mainloop()

    #Блок выхода или продолжения
    print("Введите 0 для выхода или любой символ для продолжения!")
    ExitCode=str(input())
