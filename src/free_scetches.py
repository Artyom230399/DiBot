import telebot
from telebot import types

from secret_token import token

bot = telebot.TeleBot(token)


def get_free_scetches(message):
    bot.send_message(
        message.chat.id,
        text='─── ⋆⋅☆⋅⋆ ───'
    )

    bot.send_media_group(
        message.chat.id,
        [
            telebot.types.InputMediaPhoto(open('image/free_scetches/1_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/2_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/3_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/4_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/5_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/6_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/7_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/8_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/9_p1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/10_p1.jpg', 'rb')),


        ],
    )

    keyboard = types.InlineKeyboardMarkup()

    key_next = types.InlineKeyboardButton(text='Смотреть ещё', callback_data='next_3')
    keyboard.add(key_next)

    key_back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard.add(key_back)

    bot.send_message(
        message.chat.id,
        text=
        """
        Вшему вниманию предлагаются мои эскизы 😊
         - Они абсолютно оригинальны
         - Такой больше ни у кого не будет
        """,
        reply_markup=keyboard
    )


def get_free_scetches_2(message):
    bot.send_message(
        message.chat.id,
        text='─── ⋆⋅☆⋅⋆ ───'
    )

    bot.send_media_group(
        message.chat.id,
        [
            telebot.types.InputMediaPhoto(open('image/free_scetches/11_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/12_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/13_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/14_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/15_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/16_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/17_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/18_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/19_p2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/20_p2.jpg', 'rb')),
        ],
    )

    keyboard = types.InlineKeyboardMarkup()

    key_next = types.InlineKeyboardButton(text='Смотреть ещё', callback_data='next_4')
    keyboard.add(key_next)

    key_back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard.add(key_back)

    bot.send_message(
        message.chat.id,
        text=
        """
        Рад, что заинтересовал тебя ❤️
        """,
        reply_markup=keyboard
    )


def get_free_scetches_3(message):
    bot.send_message(
        message.chat.id,
        text='─── ⋆⋅☆⋅⋆ ───'
    )

    bot.send_media_group(
        message.chat.id,
        [
            telebot.types.InputMediaPhoto(open('image/free_scetches/21_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/22_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/23_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/24_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/25_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/26_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/27_p3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('image/free_scetches/28_p3.jpg', 'rb')),
        ],
    )

    keyboard = types.InlineKeyboardMarkup()

    key_back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard.add(key_back)

    bot.send_message(
        message.chat.id,
        text=
        """
        🔥 Присоединяйся к группе, там появляются новые эскизы - https://vk.com/shodisan_tattoo
        """,
        reply_markup=keyboard
    )
