from tkinter import *
from tkinter import messagebox as mb
import random
root = Tk()
root.title('Tic-tac-toe')
game_run = True
field = []
cross_count = 0

def new_game():
    """ Функция обновляет игровое поле и переменные game_run,  cross_count, начинает игру заново """
    for row in range(10):
        for col in range(10):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = '#CCCCFF'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0
    root.title('Tic-tac-toe')

def click(row, col):
    """ Функция обрабатывает ход игрока и вызывает ответный ход компьютера """
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_lose('X', 'You')
        if game_run and cross_count < 50:
            computer_move()
            check_lose('O', 'Computer')

def check_lose(smb, player):
    """ Функция проверяет есть ли на поле 5 одинаковых символов в ряд по вертикали горизонтали и диагоналям """
    for row in range(10):
        for col in range(10):
            if col < 6:
                check_line(field[row][col], field[row][col + 1], field[row][col + 2], field[row][col + 3], field[row][col+ 4], smb, player)
            if row < 6:
                check_line(field[row][col], field[row + 1][col], field[row + 2][col], field[row + 3][col], field[row + 4][col], smb, player)
            if row < 6 and col < 6:
                check_line(field[row][col], field[row + 1][col + 1], field[row + 2][col + 2], field[row + 3][col + 3], field[row + 4][col + 4], smb, player)
                check_line(field[row + 4][col], field[row + 3][col + 1], field[row + 2][col + 2], field[row + 1][col + 3], field[row][col + 4], smb, player)

def check_line(a1,a2,a3,a4,a5,smb, player):
    """ Функция проверяет одинаковы ли 5 входящих символов, если да, то открывает всплывающее окно"""
    if a1['text'] == a2['text'] == a3['text'] == a4['text'] == a5['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = a4['background'] = a5['background'] = '#CC0000'
        global game_run
        game_run = False
        root.title(player + ' lose!')
        mb.showinfo(
            "Game over",
            player + ' lose!')

def computer_move():
    """ Функция делает один ход компьютера """
    while True:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

""" Игровое поле, графический интерфейс """
for row in range(10):
    line = []
    for col in range(10):
        button = Button(root, text=' ', width=2, height=1,
                        font=('Verdana', 20, 'bold'),
                        background='#CCCCFF',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='new game',font=('Verdana', 14, 'bold'), command=new_game)
new_button.grid(row=10, column=0, columnspan=10, sticky='nsew')
root.mainloop()
