# coding=utf-8
import telebot
import logging

bot = telebot.TeleBot('1163114593:AAFGXPuRouF8Sx-kOh0nkFU3sWSFieuYnO4')
name = ''
surname = ''
clas = ''
slov = {}


def main(use_logging, level_name):
    if use_logging:
        telebot.logger.setLevel(logging.getLevelName(level_name))
    bot.polling(none_stop=True, interval=1)


@bot.message_handler(commands=['start'])
def start_message(mess):
    global name
    sent = bot.send_message(mess.chat.id, 'Привет, Как тебя зовут?')
    print(mess.chat.id)
    slov[mess.chat.id] = ['start']
    print(slov)
    bot.register_next_step_handler(sent, surname_message)


@bot.message_handler(commands=['help'])
def help_message(mess):
    bot.send_message(mess.chat.id, '/start')


def surname_message(message):
    global name
    if len(slov[message.chat.id]) > 0:
        slov[message.chat.id].append(message.text)
        sent = bot.send_message(message.chat.id, f'{slov[message.chat.id][1].capitalize()} как ваша фамилия?')
        print(slov)
        bot.register_next_step_handler(sent, class_message)


def class_message(message):
    global name, surname
    if len(slov[message.chat.id]) > 1:
        slov[message.chat.id].append(message.text)
        sent = bot.send_message(message.chat.id,
                                f'{slov[message.chat.id][2].capitalize()}'
                                f' {slov[message.chat.id][1].capitalize()} в каком вы классе'
                                f'(написать через нижние подчеркивание, пример 10_1)')
        print(slov)
        bot.register_next_step_handler(sent, end_message)


def end_message(message):
    global clas, name, surname
    if len(slov[message.chat.id]) > 2:
        slov[message.chat.id].append(message.text)
        sent = bot.send_message(message.chat.id, f'{slov[message.chat.id][2].capitalize()}'
                                                 f' {slov[message.chat.id][1].capitalize()}'
                                                 f' {slov[message.chat.id][3]} верно?')
        print(slov)
        bot.register_next_step_handler(sent, yes_no_message)


def yes_no_message(message):
    if message.text.lower() == 'да':
        a = slov.pop(message.chat.id)
        pass
    else:
        a = slov.pop(message.chat.id)
        sent = bot.send_message(message.chat.id, 'Давай заново. Как тебя зовут')
        slov[message.chat.id] = ['start']
        print(slov)
        bot.register_next_step_handler(sent, surname_message)


print(name, surname, clas)

if __name__ == '__main__':
    main(True, 'DEBUG')
