from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from moduls import start, win, board
from random import randint

c = board()

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

        if win(c) or c.count('X  ') == 5:
            await update.message.reply_text(f'{c[0]}       {c[1]}       {c[2]}\n\n{c[3]}       {c[4]}       {c[5]}\n\n{c[6]}       {c[7]}       {c[8]}\n')
            if c.count('X  ') == 5 and not win(c): await update.message.reply_text(f'Ничья')
            else: await update.message.reply_text(f'{win(c)}')
            count = 0
            for i in c:
                count += 1
                if i == "X  ": c[count - 1] = (f'/{count}')
                if i == "O  ": c[count - 1] = (f'/{count}')
    else:
        await update.message.reply_text(f'эта клетка уже выбрана')
    await update.message.reply_text(f'{c[0]}       {c[1]}       {c[2]}\n\n{c[3]}       {c[4]}       {c[5]}\n\n{c[6]}       {c[7]}       {c[8]}\n')

app = ApplicationBuilder().token("YOUR TOKEN HERE").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("1" , step))
app.add_handler(CommandHandler("2" , step))
app.add_handler(CommandHandler("3" , step))
app.add_handler(CommandHandler("4" , step))
app.add_handler(CommandHandler("5" , step))
app.add_handler(CommandHandler("6" , step))
app.add_handler(CommandHandler("7" , step))
app.add_handler(CommandHandler("8" , step))
app.add_handler(CommandHandler("9" , step))
app.run_polling()
