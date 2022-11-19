from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# token = "Место для токена"


def echo(update, context):
    text = update.message.text
    if text.lower() in ['привет', 'приветик','ку']:
        text = "привет!"
        if text.lower() in ['пока', 'прощай','пок']:
            text = "пока!"

    update.message.reply_text(f"{text}")

def help(update, context):
    update.message.reply_text("cписок команд \n • /help - вывод доступных команд")


def start(update, context):
    update.message.reply_text("привет! \nнабери /help, чтобы просмотреть список команд")


def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    print("Бот запущен")

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()