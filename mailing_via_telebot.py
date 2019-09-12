import telebot
from time import sleep
token = "929014450:AAHqLvrvNrsEOqTNm7mbSKjRLb0eNNROp6E"
bot = telebot.TeleBot(token)

#chat_id=405204397
#bot.send_message(chat_id, 'Кd')
#photo = open("map-of-world.jpg",'rb')
#bot.send_photo(chat_id,photo)
sleep(0.25)
file_=open('some.txt','r')

for lines in file_:
	bot.send_message(lines, 'аааааааааааааааааааааааааа')

	sleep(1)
file_.close()	
#405204397 - mine chat id
#Сделать цикл for и пройтись по каждому студенту , в конце
#time.sleep(1)
'''
from telegram.ext import Updater, messagequeue as mq

@mq.queuedmessage
def send_message(bot, job):
        for user in get_subscribed(db):
            text = 'Это тестовое сообщение'
            bot.sendMessage(chat_id=user['chat_id'], text=text)
'''
