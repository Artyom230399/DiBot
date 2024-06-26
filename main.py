import telebot
from telebot import types

from secret_token import token
from src.menu import get_back_menu
from src.free_scetches import get_free_scetches, get_free_scetches_2, get_free_scetches_3
from src.my_works import get_my_works, get_my_works_2, get_my_works_3

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(
        message.chat.id,
        text='─── ⋆⋅☆⋅⋆ ───'
    )

    photo = open('image/base_photo.jpg', 'rb')
    keyboard = types.InlineKeyboardMarkup()

    key_my_works = types.InlineKeyboardButton(text='Мои работы', callback_data='my_works')
    keyboard.add(key_my_works)

    key_free_scetches = types.InlineKeyboardButton(text='Свободные эскизы', callback_data='free_scetches')
    keyboard.add(key_free_scetches)

    key_ign_up = types.InlineKeyboardButton(text='Записаться', callback_data='sign_up')
    keyboard.add(key_ign_up)

    bot.send_photo(
        message.chat.id,
        photo,
        caption="""
        👋 Привет! 
        Дильшод у аппарата. 
        Я - тату-мастер с богатым опытом, который воплотит любую твою идею в реальность 😊

        ℹ️ Немного информации обо мне -
            - Аккуратен
            - Дотошен
            - Забочусь о вашем самочувствие и удобстве
            - Работаю в студии
            - Использую одноразовые расходники
            - Дарю крем для заживления после сеанса
            - Бесплатно разрабатываю эскиз

        🎨 Основные нарправления моего творчества - 
            - Графика
            - Блэкворк
            - Япония
        """,
        reply_markup=keyboard
    )

    with open('chat_ids.txt', 'a') as f:
        f.write(str(message.chat.id) + '\n')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # main
    if call.data == "my_works":
        get_my_works(call.message)
    elif call.data == "free_scetches":
         get_free_scetches(call.message)
    elif call.data == "sign_up":
         pass

    elif call.data == "back":
        get_back_menu(call.message)

    # my_works
    elif call.data == "next":
        get_my_works_2(call.message)
    elif call.data == "next_2":
        get_my_works_3(call.message)

    # free_scetches
    elif call.data == "next_3":
        get_free_scetches_2(call.message)
    elif call.data == "next_4":
        get_free_scetches_3(call.message)


bot.polling(none_stop=True, interval=0)
