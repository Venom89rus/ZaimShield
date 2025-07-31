import telebot
from api import self
from telebot import types


bot = telebot.TeleBot(self)


#  Ответ бота на команды старт
@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = (
        "👋 Добро пожаловать в *ZaimShield* 🛡\n\n"
        "📌 *ВАЖНО*: Бот не является финансовой организацией и не выдаёт займы.\n"
        "Он создан исключительно для помощи заемщикам:\n"
        "— Разобраться в условиях микрозаймов\n"
        "— Избежать скрытых комиссий и переплат\n"
        "— Не платить за навязанные услуги и страховки или помощь вернуть выплату по страховке\n\n"
        "📊 Мы даём информацию — выбор за вами."
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown')


    text = (
        "🙏 *Команда ZaimShield оформляет займы за собственные средства*, чтобы проверить:\n"
        "— комиссии\n"
        "— сроки обработки\n"
        "— скрытые условия и возврат страховок\n\n"
        "Если бот оказался полезен, вы можете *поддержать проект* — нажав кнопку ниже.\n\n"
        "💸 Донат добровольный и ни к чему не обязывает, но нам будет приятно и важно понимать, что мы не зря стараемся.\n\n"
        "Спасибо за вашу поддержку ❤️"
    )
    markup = types.InlineKeyboardMarkup()
    donate_btn = types.InlineKeyboardButton("💖 Помощь в развитии проекта", url="https://your-donation-link.com")
    markup.add(donate_btn)
    bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode='Markdown')


    markup = types.ReplyKeyboardMarkup()
    mkk = types.KeyboardButton('Выберите компанию')
    markup.row(mkk)
    feedback = types.KeyboardButton('Обратная связь')
    markup.row(feedback)
    donat = types.KeyboardButton('Помощь в развитии проекта')
    markup.row(donat)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup = markup)

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