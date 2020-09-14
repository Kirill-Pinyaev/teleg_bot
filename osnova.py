import telebot

bot = telebot.TeleBot('1163114593:AAFGXPuRouF8Sx-kOh0nkFU3sWSFieuYnO4')
bot.polling(none_stop=True, interval=0)


@bot.message_handler(content_types=['text'])
def get_message(mess):
    print(mess)
    if mess.text == 'Привет':
        bot.send_message(mess.from_user.id, 'Привет, я могу чем помочь?')
    elif mess.text == '/help':
        bot.send_message(mess.from_user.id, 'Нариши привет')
    else:
        bot.send_message(mess.from_user.id, 'Я тебя не понимаю')
