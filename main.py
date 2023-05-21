import telebot
import os

bot = telebot.TeleBot('your token')
users = [123] #your chat id (or a few ids) 

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id not in users:
        bot.send_message(message.chat.id, "Sorry, you are not the boss")
    else:
        bot.send_message(message.from_user.id, "👋 WELCOME, KING")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.chat.id not in users:
        bot.send_message(message.chat.id, "Sorry, you are not the boss")
    else:
        pipe = os.popen(message.text+" 2>&1")
        text = pipe.read()
        if text == "": text = "completed"
        bot.send_message(message.from_user.id, text)        

bot.polling(none_stop=True, interval=0)
