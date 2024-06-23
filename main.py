import telebot

from secret_token import token

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    photo = open('image/base_photo.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, caption="""
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
    """)

    with open('chat_ids.txt', 'a') as f:
        f.write(str(message.chat.id) + '\n')


bot.polling(none_stop=True, interval=0)
