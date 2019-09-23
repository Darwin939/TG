import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from main_func import parse_name
from main_func import department
from main_func import last_sem_gpa
from main_func import get_course

name =''
department_ = ''
last_gpa = ''
course = ''


true_f = True
df =pd.DataFrame({"id":[],'full_name':[],'department':[],
	'last_gpa':[],'course':[]}) # проверить на повторное использование	

min_var = 41711250#minimum var

def main_circle(stud_id):
	session = requests.Session()
	request = session.get(f"http://student.kazgasa.kz/Students/{stud_id}.htm")
	if request.status_code ==200:
		
			###########
		name = parse_name(stud_id)
		department_ = department(stud_id)
		last_gpa = last_sem_gpa(stud_id)
		course = get_course(stud_id)
		data = [stud_id,name,department_,last_gpa,course]
		df.loc[-1] = data
		df.index = df.index + 1		 
		
		
	else:
		pass


while true_f == True:
	if min_var == 41711260:
		true_f = False
		
	else:
		main_circle(min_var)
		min_var+=1
		print (min_var)
df.to_csv('filename.csv')
