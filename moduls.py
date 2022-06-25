from telegram import Update
from telegram.ext import ContextTypes
from random import randint
c = ['/1','/2','/3','/4','/5','/6','/7','/8','/9']


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    restart(c)
    await update.message.reply_text(f'{c[0]}       {c[1]}       {c[2]}\n\n{c[3]}       {c[4]}       {c[5]}\n\n{c[6]}       {c[7]}       {c[8]}\n')

    
def restart(c):
    count = 0
    for i in c:
        count += 1
        if i == "X  ": c[count - 1] = (f'/{count}')
        if i == "O  ": c[count - 1] = (f'/{count}')

            
async def step(update: Update, context: ContextTypes.DEFAULT_TYPE):
    player = int(update.message.text[1:])
    if (str(c[player - 1]) not in "X  O  "):
        c[player - 1] = 'X  '
        if c.count('X  ') < 5:
            complete = False
            while not complete:
                computer = randint(1, 9)
                if (str(c[computer - 1]) not in "X  O  "):
                    c[computer - 1] = 'O  '
                    complete = True
        if win(c):
            await update.message.reply_text(f'{c[0]}       {c[1]}       {c[2]}\n\n{c[3]}       {c[4]}       {c[5]}\n\n{c[6]}       {c[7]}       {c[8]}\n')
            await update.message.reply_text(f'{win(c)}')
            restart(c)
    else:
        await update.message.reply_text(f'эта клетка уже выбрана')
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
    if count == 3 or c.count('X  ') == 5:
        winner = 'Ничья'
        return winner
