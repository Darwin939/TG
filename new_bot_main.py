import telebot
from telebot import types
import imgkit



token = "929014450:AAHqLvrvNrsEOqTNm7mbSKjRLb0eNNROp6E"
bot = telebot.TeleBot(token)
markup = types.ReplyKeyboardMarkup(row_width=3)
itembtn1 = types.KeyboardButton('Реквизиты')
itembtn2 = types.KeyboardButton('F.A.Q')
itembtn3 = types.KeyboardButton('Sholarships')
itembtn4 = types.KeyboardButton('Транскрипт')
itembtn5 = types.KeyboardButton('Узнать свой последний рейтинг')
itembtn6 = types.KeyboardButton('Расписание занятий(exc)')
markup.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5,itembtn6)

@bot.message_handler(commands=['start'])
def start(message):
	
	bot.send_message(message.chat.id, 'Привет, Выбери одну из команд',reply_markup=markup)
	
	with open('some.txt','a') as file:
		file.write((str(message.chat.id)+'\n'))
	
@bot.message_handler(content_types=['text'])
def text_handler(message):
	if message.text == "Реквизиты":
		rekv_photo=open('rekv.png','rb')
		bot.send_photo(message.chat.id,rekv_photo,reply_markup=markup)
		rekv_photo.close
		start(message)
	elif message.text == 'F.A.Q':
		bot.send_message(message.chat.id, 'Какой-то текст или ссылка',reply_markup=markup)
	elif message.text == 'Sholarships':
		cholar_photo=open('table_of_cholar.png','rb')
		bot.send_photo(message.chat.id,cholar_photo,reply_markup=markup)	
		cholar_photo.close()
	elif message.text == 'Вопросы Оплаты':
		msg = bot.send_message(message.chat.id, 'Здесь должны быть ответы на часто задаваемые вопросы оплаты',reply_markup=markup)
	elif message.text == 'Узнать свой последний рейтинг':
		msg = bot.send_message(message.chat.id, 'Какой ваш ID?')
		bot.register_next_step_handler(msg,text_jpg)
	elif message.text == 'Расписание занятий(exc)':
		doc = open('table_fos.xls','rb')
		bot.send_document(message.chat.id, doc,reply_markup=markup)
		doc.close()
	elif message.text == 'Транскрипт':
		msg = bot.send_message(message.chat.id, 'Какой ваш ID?')
		bot.register_next_step_handler(msg,text_jpg)	
	else:
		start(message)#нужен help
def text_jpg(message):
	print (message.text)
	if message.text.isdigit():
		
		img = imgkit.from_url(f'http://student.kazgasa.kz/Comments/{message.text}.htm',False)#нужно менять config
		bot.send_photo(message.chat.id,img)
		start(message)
'''
		except:
			bot.send_message(message.chat.id, "Неправильный id")
			start(message) 
'''

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print (e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15) 

