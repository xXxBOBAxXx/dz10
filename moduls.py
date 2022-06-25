from telegram import Update
from telegram.ext import ContextTypes

def board():
    c = ['/1','/2','/3','/4','/5','/6','/7','/8','/9']
    return c

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    c = board()
    await update.message.reply_text(f'{c[0]}       {c[1]}       {c[2]}\n\n{c[3]}       {c[4]}       {c[5]}\n\n{c[6]}       {c[7]}       {c[8]}\n')

def win(c):
    lines = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    count = 0
    for i in lines:
        if c[i[0]] == c[i[1]] == c[i[2]] == 'X  ': count += 1
        if c[i[0]] == c[i[1]] == c[i[2]] == 'O  ': count += 2
    if count == 1:
        winner = 'Вы выйграли'
        return winner
    if count == 2:
        winner = 'Выйграл компьютер'
        return winner
    if count == 3:
        winner = 'Ничья'
        return winner
    

