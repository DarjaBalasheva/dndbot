import telebot
import random
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

bot = telebot.TeleBot('6684103620:AAEnEcxbTqVPiRi0Z73ajGMoSSA0ao5tglg')


@bot.message_handler(commands=['start', 'help']) #@ -
def start_command(message):
    user_name = message.chat.first_name  # имя пользователя
    user_id = message.chat.id

    text = (f"Приветсвую тебя, {user_name}! "
            f"Здесь ты можешь поиграть в классическую РПГ игру."
            f"Нажми на /start_game для запуска")

    start_keyboard = ReplyKeyboardMarkup()
    btn_random_int = KeyboardButton('Назови число')
    start_keyboard.add(btn_random_int)
    bot.send_message(chat_id=user_id, text=text, reply_markup=start_keyboard)
    # bot.send_message(chat_id=1124334301, text='Bot starting')


@bot.message_handler(commands=['inline'])
def inline_command(message):
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text='Кнопка один', callback_data="1")
    btn2 = InlineKeyboardButton(text = 'Кнопка два', callback_data="2")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Выбери кнопку", reply_markup = markup)


@bot.callback_query_handler(func=lambda call: True)
def get_callback(call):
    print(call)
    print(call.data)
    user_id = call.from_user.id
    message_id = call.message.message_id
    if call.data == '1':
        bot.send_message(chat_id=user_id, text='Ты нажал первую кнопку')
    elif call.data == '2':
        bot.send_message(chat_id=user_id, text='Ты нажал вторую кнопку')
    bot.delete_message(chat_id=user_id, message_id=message_id)



@bot.message_handler(regexp='Назови число')
def send_random_int(message):
    rand_int = str(random.randint(0, 100))
    user_id = message.chat.id
    bot.send_message(chat_id=user_id, text=rand_int)


@bot.message_handler(content_types=['text'])
# content_types=['audio', 'photo', 'voice', 'video', 'document',
#                 'text', 'location', 'contact', 'sticker'])
def repeat(message):
    print(message)
    print(type(message))
    bot.send_message(message.chat.id, message.text)  #1112233344455


bot.polling(non_stop=True)  # Бот рабоает, пока не остановим вручную
