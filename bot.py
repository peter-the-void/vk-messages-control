import telebot
import chat_messages as cm
from vk_messages_control import Message, User
bot = telebot.TeleBot('288577480:AAHLCAz53rhF0T14CL80qJLIiPdbupqbvbc')

user = User('harovod@mail.ru','kinoprom12')
user.auth()

@bot.message_handler(commands=['start'])
def hello_message(message):
	bot.send_message(message.chat.id, cm.hello_msg(message.chat.first_name, message.chat.last_name))


@bot.message_handler(commands=['get'])
def get_message_from_vk(message):
	messages = user.get_messages()
	print(messages)
	for msg in messages:
		bot.send_message(message.chat.id, msg)


if __name__ == '__main__':
     bot.polling(none_stop=True)
