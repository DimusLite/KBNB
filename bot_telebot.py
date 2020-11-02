import telebot

TOKEN = "705130797:AAGoiH-ru25oKOgAmTP1qiMNAh5wB0FBtaY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здароф, я бот-секретарь')

bot.polling()