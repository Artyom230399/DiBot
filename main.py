import telebot
from telebot import types

from secret_token import token

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


def get_back_menu(message):
    bot.send_message(
        message.chat.id,
        text='─── ⋆⋅☆⋅⋆ ───'
    )

    keyboard = types.InlineKeyboardMarkup()

    key_my_works = types.InlineKeyboardButton(text='Мои работы', callback_data='my_works')
    keyboard.add(key_my_works)

    key_free_scetches = types.InlineKeyboardButton(text='Свободные эскизы', callback_data='free_scetches')
    keyboard.add(key_free_scetches)

    key_ign_up = types.InlineKeyboardButton(text='Записаться', callback_data='sign_up')
    keyboard.add(key_ign_up)

    bot.send_message(
        message.chat.id,
        text=
        """
        😊 Тут можно узнать меня лучше
        """,
        reply_markup=keyboard
    )


def get_my_works(message):
    bot.send_message(
        message.chat.id,
        text='─── ⋆⋅☆⋅⋆ ───'
    )

    bot.send_media_group(
        message.chat.id,
        [
            telebot.types.InputMediaPhoto(open('image/my_works/1_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/2_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/3_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/4_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/5_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/6_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/7_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/8_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/9_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/10_p1.jpg', 'rb')),
        ],
    )

    keyboard = types.InlineKeyboardMarkup()

    key_next = types.InlineKeyboardButton(text='Смотреть ещё', callback_data='next')
    keyboard.add(key_next)

    key_back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard.add(key_back)

    bot.send_message(
        message.chat.id,
        text=
        """
        ⚠️ Каждый эскиз оригинален 
        От тебя требуется только референс, наброски или идея 💡
        """,
        reply_markup=keyboard
    )


def get_my_works_2(message):
    bot.send_message(
        message.chat.id,
        text='─── ⋆⋅☆⋅⋆ ───'
    )

    bot.send_media_group(
        message.chat.id,
        [
            telebot.types.InputMediaPhoto(open('image/my_works/11_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/12_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/13_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/14_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/15_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/16_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/17_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/18_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/19_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/20_p2.jpg', 'rb')),
        ],
    )

    keyboard = types.InlineKeyboardMarkup()

    key_next = types.InlineKeyboardButton(text='Смотреть ещё', callback_data='next_2')
    keyboard.add(key_next)

    key_back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard.add(key_back)

    bot.send_message(
        message.chat.id,
        text=
        """
        😊 Вот еще немного моих работ
        """,
        reply_markup=keyboard
    )


def get_my_works_3(message):
    bot.send_message(
        message.chat.id,
        text='─── ⋆⋅☆⋅⋆ ───'
    )

    bot.send_media_group(
        message.chat.id,
        [
            telebot.types.InputMediaPhoto(open('image/my_works/21_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/22_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/23_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/24_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/25_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/26_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/27_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/28_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/29_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/my_works/30_p3.jpg', 'rb')),
        ],
    )

    keyboard = types.InlineKeyboardMarkup()

    key_back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard.add(key_back)

    bot.send_message(
        message.chat.id,
        text=
        """
        🔥 Еще больше не менее крутых моих работ ты можешь найти тут - https://vk.com/shodisan_tattoo
        """,
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "my_works":
        get_my_works(call.message)
    elif call.data == "free_scetches":
         pass
    elif call.data == "sign_up":
         pass

    elif call.data == "back":
        get_back_menu(call.message)

    elif call.data == "next":
        get_my_works_2(call.message)
    elif call.data == "next_2":
        get_my_works_3(call.message)


bot.polling(none_stop=True, interval=0)
