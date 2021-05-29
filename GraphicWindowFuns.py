# Функции для создания графического интерфейса с кнопками
import operator
import tkinter as tk
import os
import ctypes
from ctypes import windll
# from ctypes import *
import re

def make_window():
    """Установка оптимального интерфейса"""
    x = (windll.user32.GetSystemMetrics(0))//8
    y = (windll.user32.GetSystemMetrics(1))//8
    os.system('mode con cols=' + str(x) + ' lines=' + str(y))
    os.system('color 2f')


def make_ui():
    """Блок открытия приветственного окна """
    win = open_up()
    Btn = tk.Button(text="Начать игру!", command=win.destroy, padx="20", pady="8", fg="red", bg="yellow", )
    write("Добро пожаловать на Поле Чудес!")
    Btn.pack()
    win.mainloop()

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
    c = a + b
    label = tk.Label(
        text=c,
        font="Times 15",
        fg="blue",
        bg="pink",
        width=240,
        height=30,
    )
    label.pack()
