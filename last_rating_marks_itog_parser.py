import requests
from bs4 import BeautifulSoup as bs
import requests

def group_parse(user_id, headers={'accept': '*/*','user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36'}):
#find group, and return this var    
	session = requests.Session()
	request = session.get(f"http://student.kazgasa.kz/Comments/{user_id}.htm")
	if request.status_code == 200:
		soup = bs(request.content, "html.parser")
		name = soup.find_all('td')
		
		for line in (name):
			if line.text=="ГиК-17-1*":
				
				return line.text
			else:
				pass		
	else:
		pass

