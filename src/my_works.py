import telebot
from telebot import types

from secret_token import token

bot = telebot.TeleBot(token)


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
        Каждый эскиз оригинален ⚠️ 
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
        Вот еще немного моих работ 😊
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
