import pandas as pd
from main_func import parse_name
from main_func import department
from main_func import last_sem_gpa
from main_func import get_course
name =''
department_ = ''
last_gpa = ''
course = ''
def ret_list(stud_id):
#return list	
	name = parse_name(stud_id)
	department_ = department(stud_id)
	last_gpa = last_sem_gpa(stud_id)
	course = get_course(stud_id)
	data = [stud_id,name,department_,last_gpa,course]
	return data
#create df
df =pd.DataFrame({"id":[],'full_name':[],'department':[],
	'last_gpa':[],'course':[]}) # проверить на повторное использование	
def save_df(stud_id):
#save file to dataframe in pandas
# индексы в убывающем порядке
#первые сверху
	df.loc[-1] = ret_list(stud_id)
	df.index = df.index + 1
	return df
	
print (save_df('41711251'))
print (save_df("41711283"))
df.to_csv('filename.csv')
'''
s1 = pd.Series([5, 6, 7])
s2 = pd.Series([7, 8, 9])

df = pd.DataFrame([list(s1), list(s2)],  columns =  ["A", "B", "C"])



print (df)

df.loc[-1] = [2, 3, 4]
print (df)
df.index = df.index + 1
print (df)
'''
