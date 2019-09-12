def text_jpg(message):
	if message.isdigit():
		try:
			img = imgkit.from_url(f'http://student.kazgasa.kz/Students/{message}.htm',False)#нужно менять config
			bot.send_photo(chat_id,img)
			help_us(message)
		except:
			bot.send_message(chat_id, "Неправильный id")
			start(message)
	else:
		start(message) 
