import telebot


bot = telebot.TeleBot('7640149172:AAG-5TTFeTpSYQF2I5FBLbhgvzeimYfguGE')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')

bot.polling(none_stop = True)