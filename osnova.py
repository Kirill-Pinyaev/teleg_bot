# coding=utf-8
import telebot
import logging

bot = telebot.TeleBot('1163114593:AAFGXPuRouF8Sx-kOh0nkFU3sWSFieuYnO4')
name = ''
surname = ''
clas = ''


def main(use_logging, level_name):
    if use_logging:
        telebot.logger.setLevel(logging.getLevelName(level_name))
    bot.polling(none_stop=True, interval=1)


@bot.message_handler(commands=['start'])
def start_message(mess):
    global name
    sent = bot.send_message(mess.from_user.id, 'Привет, Как тебя зовут?')
    bot.register_next_step_handler(sent, surname_message)


@bot.message_handler(commands=['help'])
def help_message(mess):
    bot.send_message(mess.from_user.id, '/start')


def surname_message(message):
    global name
    name = message.text
    sent = bot.send_message(message.chat.id, f'{name.capitalize()} как ваша фамилия?')
    bot.register_next_step_handler(sent, class_message)


def class_message(message):
    global name, surname
    surname = message.text
    sent = bot.send_message(message.from_user.id,
                            f'{surname.capitalize()} {name.capitalize()} в каком вы классе'
                            f'(написать через нижние подчеркивание, пример 10_1)')
    bot.register_next_step_handler(sent, end_message)


def end_message(message):
    global clas, name, surname
    clas = message.text
    sent = bot.send_message(message.chat.id, f'{surname.capitalize()} {name.capitalize()} {clas} верно?')
    bot.register_next_step_handler(sent, yes_no_message)


def yes_no_message(message):
    if message.text.lower() == 'да':
        pass
    else:
        sent = bot.send_message(message.from_user.id, 'Давай заново. Как тебя зовут')
        bot.register_next_step_handler(sent, surname_message)


print(name, surname, clas)

if __name__ == '__main__':
    main(True, 'DEBUG')
