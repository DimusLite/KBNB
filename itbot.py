from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler
from telegram.ext import Filters

def message_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Пример текста',
    )

def main():
    print('Start')
    updater = Updater(
        token='705130797:AAGoiH-ru25oKOgAmTP1qiMNAh5wB0FBtaY',
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()