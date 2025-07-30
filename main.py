import telebot
from api import self
from telebot import types


bot = telebot.TeleBot(self)


#  Ответ бота на команды старт
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    markup = types.ReplyKeyboardMarkup()
    mkk = types.KeyboardButton('Выберите компанию')
    markup.row(mkk)
    blank = types.KeyboardButton('Бланки')
    adress = types.KeyboardButton('E-mail MKK')
    markup.row(blank,adress)
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '<b>Help information</b>', parse_mode='html')

# Ответ Бота на типы файлов
@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')

    elif message.text.lower() == 'id':
        bot.reply_to(message, f'Ваш id в системе: {message.from_user.id}')

    elif message.text.lower() == 'info':
        bot.reply_to(message, f'{message.from_user.first_name}, данный Бот постарается тебе показать все подводные камни при взятии займа!')

@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.reply_to(message, f'{message.from_user.first_name}, красивое фото!' )


# Цикличная работа бота
bot.polling(none_stop = True)