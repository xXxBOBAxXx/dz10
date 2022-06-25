from telegram.ext import ApplicationBuilder, CommandHandler
from moduls import start, step

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
