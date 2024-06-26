import telebot
from telebot import types

from secret_token import token

bot = telebot.TeleBot(token)


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
        Тут можно узнать меня лучше ℹ️ 
        """,
        reply_markup=keyboard
    )
