import requests
from bs4 import BeautifulSoup as bs

def parse_name(user_id):
#Парсит имена студентов
#Возвращает имена
	session = requests.Session()
	request = session.get(f"http://student.kazgasa.kz/Students/{user_id}.htm")
	if request.status_code ==200:
		soup = bs(request.content,"html.parser") 
		name = soup.find_all('table')[1].find_all('tr')[2].find_all('td')[1].text
		return name
	else:
		print ("Status code 400")

def department(user_id):
#возвращает его специальность 
# для гиков - специальность
# для архов и фосов его факультет , для тдо и т.д их специальность
	session = requests.Session()
	request = session.get(f"http://student.kazgasa.kz/Students/{user_id}.htm")
	if request.status_code ==200:
		soup = bs(request.content,"html.parser") 
		dep = soup.find_all('table')[1].find_all('tr')[3].find_all('td')[1].text
		return dep
	else:
		print ("bad request")
		


def last_sem_gpa(user_id):
#возвращает его поселдний gpa
	session = requests.Session()
	request = session.get(f"http://student.kazgasa.kz/Students/{user_id}.htm")
	if request.status_code ==200:
		soup = bs(request.content,"html.parser") 
		gpa = soup.find_all('table')[-1].find_all('tr')[-3].find_all('td')[1].text
		return gpa
	else:
		print ("Status code 400")
def get_course(user_id):
#брать его курс
# возвращает его курс
	session = requests.Session()
	request = session.get(f"http://student.kazgasa.kz/Students/{user_id}.htm")
	if request.status_code ==200:
		soup = bs(request.content,"html.parser") 
		course = soup.find_all('table')[1].find_all("tr")[4].find_all("td")[3].text
		return get_year(course)
	else:
		print ("Status code 400")

def get_year(date):
	data=date.split(".")
	year = data[2]
	if year == "2015":
		return 5
	if year == "2016":
		return 4
	if year == "2017":
		return 3
	if year == "2018":
		return 2
	if year == "2019":
		return 1
	else:
		print ("Какой курс или без данных ?")


