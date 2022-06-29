import telebot as tb
from telebot import types
import time



token = open('token.txt', 'r').readline()
bot = tb.TeleBot(token)


@bot.message_handler(commands = ['start', 'help'])
def start(message):
	text = 'Hi!'
	bot.send_message(message.chat.id, text, parse_mode = "html")


while True:
    try:
        bot.polling(none_stop = True, interval = 0)
    except:
        time.sleep(10)