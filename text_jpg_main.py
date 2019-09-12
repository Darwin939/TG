import imgkit
#C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe
config = imgkit.config(wkhtmltoimage='C:/Program Files/wkhtmltopdf/bin/wkhtmltoimage.exe')
#imgkit.from_string(html_string, output_file, config=config)
def text_jpg(message):
	print (message.text)
	if message.text.isdigit():
		try:
			img = imgkit.from_url(f'http://student.kazgasa.kz/Students/{message.text}.htm',False,config=config)#нужно менять config
			bot.send_photo(message.chat.id,img)
			help_us(message)

		except:
			bot.send_message(message.chat.id, "Неправильный id")
			help_us(message)

	else:
		start(message) 
