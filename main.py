import telebot
import webbrowser

# подключаем бота через API
bot = telebot.TeleBot('7640149172:AAG-5TTFeTpSYQF2I5FBLbhgvzeimYfguGE')

# Добавляет приветствие после написания в боте "start"
@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')

# Добавляет приветствие после написания в боте "help"
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Если возникли вопросы пишите ......')

# создаем переход на сайт при указании команды 'site'
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.mail.ru')


@bot.message_handler()
def info(message):
    #      ответ при вводе слова "привет"
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')

    #       ответ на сообщение пользователя
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'Ваш ID в системе: {message.from_user.id}')


# Заставляет Бота работать циклически
bot.polling(non_stop = True)
