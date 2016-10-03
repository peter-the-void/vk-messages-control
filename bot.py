import telebot
import chat_messages as cm
import time
from vk_messages_control import auth, get_unread_messages

bot = telebot.TeleBot('262198662:AAH5dLW6jyrmbV4Tesz_BkwiUZbdkfC48Wc')
#session


@bot.message_handler(commands = ['settings'])
def settings_message(message):
	session = auth()
	print(type(session))

@bot.message_handler(commands=['start'])
def hello_message(message):
    bot.send_message(message.chat.id, cm.hello_msg(message.chat.first_name, message.chat.last_name))


@bot.message_handler(commands=['close'])
def GoodbayMessage(message):
    bot.send_message(message.chat.id, 'Goodbay, Stas!')
    _main_flag = False


if __name__ == '__main__':
    bot.polling(none_stop=True)
