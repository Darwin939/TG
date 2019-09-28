import numpy as np
import pandas as pd
def where_my_dep(text):
	first_dig=list(str(text))
	one = first_dig[0]
	third  = first_dig[2]
	
	#  fstim 2 kurs
	if one=='4' and third == '8':
		# сортирует весь фстим 2 курс
		df = pd.read_csv('bd/fstim_2.csv')
		df = df.sort_values('last_gpa',ascending=True)
		df = df.dropna().reset_index()
		df=df.iloc[::-1]
		# место в общей дб
		d = np.where(df['id']==int(text))
		# по его специальности
		dep = df.loc[df['id'] == int(text)]['department'].values[0]
		
		dep_df = df.loc[df['department'] == dep]
		dep_df = dep_df.sort_values('last_gpa',ascending=True)
		dep_df = dep_df.dropna().reset_index()
		dep_df=dep_df.iloc[::-1]
		# на каком месте он среди специальности цифра
		d =d[0][0]+1
		num = np.where(dep_df['id']==int(text))
		num =num[0][0]+1
		lendth_df=len(df.index)
		lendth_dep=len(dep_df.index)
		faculty = 'фстим 2 курс'
		# ваше место фак, из, название спец,ваше место по спецу ,из,факультет и курс
		ans = [d,lendth_df,dep,num,lendth_dep,faculty]
		return ans
	if one == '4' and third=='7':
		# сортирует весь фстим 3 курс
		df = pd.read_csv('bd/fstim_3.csv')
		df = df.sort_values('last_gpa',ascending=True)
		df = df.dropna().reset_index()
		df=df.iloc[::-1]
		# место в общей дб
		d = np.where(df['id']==int(text))
		# по его специальности
		dep = df.loc[df['id'] == int(text)]['department'].values[0]
		
		dep_df = df.loc[df['department'] == dep]
		dep_df = dep_df.sort_values('last_gpa',ascending=True)
		dep_df = dep_df.dropna().reset_index()
		dep_df=dep_df.iloc[::-1]
		# на каком месте он среди специальности цифра
		d =d[0][0]+1
		num = np.where(dep_df['id']==int(text))
		num =num[0][0]+1
		lendth_df=len(df.index)
		lendth_dep=len(dep_df.index)
		faculty = 'фстим 3 курс'
		# ваше место фак, из, название спец,ваше место по спецу ,из
		ans = [d,lendth_df,dep,num,lendth_dep,faculty]
		return ans	
	if one == '4' and third=='6':
	# сортирует весь фстим 4 курс
		df = pd.read_csv('bd/fstim_4.csv')
		df = df.sort_values('last_gpa',ascending=True)
		df = df.dropna().reset_index()
		df=df.iloc[::-1]
		# место в общей дб
		d = np.where(df['id']==int(text))
		# по его специальности
		dep = df.loc[df['id'] == int(text)]['department'].values[0]
		
		dep_df = df.loc[df['department'] == dep]
		dep_df = dep_df.sort_values('last_gpa',ascending=True)
		dep_df = dep_df.dropna().reset_index()
		dep_df=dep_df.iloc[::-1]
		# на каком месте он среди специальности цифра
		d =d[0][0]+1
		num = np.where(dep_df['id']==int(text))
		num =num[0][0]+1
		lendth_df=len(df.index)
		lendth_dep=len(dep_df.index)
		faculty = 'фстим 4 курс'
		# ваше место фак, из, название спец,ваше место по спецу ,из
		ans = [d,lendth_df,dep,num,lendth_dep,faculty]
		return ans
	if one == '1' and third=='8':
		# сортирует весь Арх 2 курс
		df = pd.read_csv('bd/arch_2.csv')
		df = df.sort_values('last_gpa',ascending=True)
		df = df.dropna().reset_index()
		df=df.iloc[::-1]
		# место в общей дб
		d = np.where(df['id']==int(text))
		# по его специальности
		dep = df.loc[df['id'] == int(text)]['department'].values[0]
		
		dep_df = df.loc[df['department'] == dep]
		dep_df = dep_df.sort_values('last_gpa',ascending=True)
		dep_df = dep_df.dropna().reset_index()
		dep_df=dep_df.iloc[::-1]
		# на каком месте он среди специальности цифра
		d =d[0][0]+1
		num = np.where(dep_df['id']==int(text))
		num =num[0][0]+1
		lendth_df=len(df.index)
		lendth_dep=len(dep_df.index)
		faculty = 'Архитектура 2 курс'
		# ваше место фак, из, название спец,ваше место по спецу ,из
		ans = [d,lendth_df,dep,num,lendth_dep,faculty]
		return ans
	if one == '1' and third=='7':
		# сортирует весь Арх 3 курс
		df = pd.read_csv('bd/arch_3.csv')
		df = df.sort_values('last_gpa',ascending=True)
		df = df.dropna().reset_index()
		df=df.iloc[::-1]
		# место в общей дб
		d = np.where(df['id']==int(text))
		# по его специальности
		dep = df.loc[df['id'] == int(text)]['department'].values[0]
		
		dep_df = df.loc[df['department'] == dep]
		dep_df = dep_df.sort_values('last_gpa',ascending=True)
		dep_df = dep_df.dropna().reset_index()
		dep_df=dep_df.iloc[::-1]
		# на каком месте он среди специальности цифра
		d =d[0][0]+1
		num = np.where(dep_df['id']==int(text))
		num =num[0][0]+1
		lendth_df=len(df.index)
		lendth_dep=len(dep_df.index)
		faculty = 'Архитектура 3 курс'
		# ваше место фак, из, название спец,ваше место по спецу ,из,факультет и курс
		ans = [d,lendth_df,dep,num,lendth_dep,faculty]
		return ans
	if one == '1' and third=='6':
		# сортирует весь Арх 4 курс
		df = pd.read_csv('bd/arch_4.csv')
		df = df.sort_values('last_gpa',ascending=True)
		df = df.dropna().reset_index()
		df=df.iloc[::-1]
		# место в общей дб
		d = np.where(df['id']==int(text))
		# по его специальности
		dep = df.loc[df['id'] == int(text)]['department'].values[0]
		
		dep_df = df.loc[df['department'] == dep]
		dep_df = dep_df.sort_values('last_gpa',ascending=True)
		dep_df = dep_df.dropna().reset_index()
		dep_df=dep_df.iloc[::-1]
		# на каком месте он среди специальности цифра
		d =d[0][0]+1
		num = np.where(dep_df['id']==int(text))
		num =num[0][0]+1
		lendth_df=len(df.index)
		lendth_dep=len(dep_df.index)
		faculty = 'Архитектура 4 курс'
		# ваше место фак, из, название спец,ваше место по спецу ,из,факультет и курс
		ans = [d,lendth_df,dep,num,lendth_dep,faculty]
		return ans
	if one == '2' and third=='6':
		# сортирует весь диз 4 курс
		df = pd.read_csv('bd/diz_4.csv')
		df = df.sort_values('last_gpa',ascending=True)
		df = df.dropna().reset_index()
		df=df.iloc[::-1]
		# место в общей дб
		d = np.where(df['id']==int(text))
		# по его специальности
		dep = df.loc[df['id'] == int(text)]['department'].values[0]
		
		dep_df = df.loc[df['department'] == dep]
		dep_df = dep_df.sort_values('last_gpa',ascending=True)
		dep_df = dep_df.dropna().reset_index()
		dep_df=dep_df.iloc[::-1]
		# на каком месте он среди специальности цифра
		d =d[0][0]+1
		num = np.where(dep_df['id']==int(text))
		num =num[0][0]+1
		lendth_df=len(df.index)
		lendth_dep=len(dep_df.index)
		faculty = 'Дизайн 4 курс'
		# ваше место фак, из, название спец,ваше место по спецу ,из,факультет и курс
		ans = [d,lendth_df,dep,num,lendth_dep,faculty]
		return ans
	if one == '2' and third=='7':
	# сортирует весь диз 3 курс
		df = pd.read_csv('bd/diz_3.csv')
		df = df.sort_values('last_gpa',ascending=True)
		df = df.dropna().reset_index()
		df=df.iloc[::-1]
		# место в общей дб
		d = np.where(df['id']==int(text))
		# по его специальности
		dep = df.loc[df['id'] == int(text)]['department'].values[0]
		
		dep_df = df.loc[df['department'] == dep]
		dep_df = dep_df.sort_values('last_gpa',ascending=True)
		dep_df = dep_df.dropna().reset_index()
		dep_df=dep_df.iloc[::-1]
		# на каком месте он среди специальности цифра
		d =d[0][0]+1
		num = np.where(dep_df['id']==int(text))
		num =num[0][0]+1
		lendth_df=len(df.index)
		lendth_dep=len(dep_df.index)
		faculty = 'Дизайн 3 курс'
		# ваше место фак, из, название спец,ваше место по спецу ,из,факультет и курс
		ans = [d,lendth_df,dep,num,lendth_dep,faculty]
		return ans
	if one == '2' and third=='8':
	# сортирует весь диз 2 курс
		df = pd.read_csv('bd/diz_2.csv')
		df = df.sort_values('last_gpa',ascending=True)
		df = df.dropna().reset_index()
		df=df.iloc[::-1]
		# место в общей дб
		d = np.where(df['id']==int(text))
		# по его специальности
		dep = df.loc[df['id'] == int(text)]['department'].values[0]
		
		dep_df = df.loc[df['department'] == dep]
		dep_df = dep_df.sort_values('last_gpa',ascending=True)
		dep_df = dep_df.dropna().reset_index()
		dep_df=dep_df.iloc[::-1]
		# на каком месте он среди специальности цифра
		d =d[0][0]+1
		num = np.where(dep_df['id']==int(text))
		num =num[0][0]+1
		lendth_df=len(df.index)
		lendth_dep=len(dep_df.index)
		faculty = 'Дизайн 2 курс'
		# ваше место фак, из, название спец,ваше место по спецу ,из,факультет и курс
		ans = [d,lendth_df,dep,num,lendth_dep,faculty]
		return ans
	if one == '2' and third=='5':
	# сортирует весь диз 5 курс
		df = pd.read_csv('bd/diz_5.csv')
		df = df.sort_values('last_gpa',ascending=True)
		df = df.dropna().reset_index()
		df=df.iloc[::-1]
		# место в общей дб
		d = np.where(df['id']==int(text))
		# по его специальности
		dep = df.loc[df['id'] == int(text)]['department'].values[0]
		
		dep_df = df.loc[df['department'] == dep]
		dep_df = dep_df.sort_values('last_gpa',ascending=True)
		dep_df = dep_df.dropna().reset_index()
		dep_df=dep_df.iloc[::-1]
		# на каком месте он среди специальности цифра
		d =d[0][0]+1
		num = np.where(dep_df['id']==int(text))
		num =num[0][0]+1
		lendth_df=len(df.index)
		lendth_dep=len(dep_df.index)
		faculty = 'Дизайн 5 курс'
		# ваше место фак, из, название спец,ваше место по спецу ,из,факультет и курс
		ans = [d,lendth_df,dep,num,lendth_dep,faculty]
		return ans
	if one == '1' and third=='5':
	# сортирует весь арх 5 курс
		df = pd.read_csv('bd/arch_5.csv')
		df = df.sort_values('last_gpa',ascending=True)
		df = df.dropna().reset_index()
		df=df.iloc[::-1]
		# место в общей дб
		d = np.where(df['id']==int(text))
		# по его специальности
		dep = df.loc[df['id'] == int(text)]['department'].values[0]
		
		dep_df = df.loc[df['department'] == dep]
		dep_df = dep_df.sort_values('last_gpa',ascending=True)
		dep_df = dep_df.dropna().reset_index()
		dep_df=dep_df.iloc[::-1]
		# на каком месте он среди специальности цифра
		d =d[0][0]+1
		num = np.where(dep_df['id']==int(text))
		num =num[0][0]+1
		lendth_df=len(df.index)
		lendth_dep=len(dep_df.index)
		faculty = 'Архитектура 5 курс'
		# ваше место фак, из, название спец,ваше место по спецу ,из,факультет и курс
		ans = [d,lendth_df,dep,num,lendth_dep,faculty]
		return ans	
	if one == '3' and third=='8':
	# сортирует весь фос 2 курс
		df = pd.read_csv('bd/fos_2.csv')
		df = df.sort_values('last_gpa',ascending=True)
		df = df.dropna().reset_index()
		df=df.iloc[::-1]
		# место в общей дб
		d = np.where(df['id']==int(text))
		# по его специальности
		dep = df.loc[df['id'] == int(text)]['department'].values[0]
		
		dep_df = df.loc[df['department'] == dep]
		dep_df = dep_df.sort_values('last_gpa',ascending=True)
		dep_df = dep_df.dropna().reset_index()
		dep_df=dep_df.iloc[::-1]
		# на каком месте он среди специальности цифра
		d =d[0][0]+1
		num = np.where(dep_df['id']==int(text))
		num =num[0][0]+1
		lendth_df=len(df.index)
		lendth_dep=len(dep_df.index)
		faculty = 'Фос 2 курс'
		# ваше место фак, из, название спец,ваше место по спецу ,из,факультет и курс
		ans = [d,lendth_df,dep,num,lendth_dep,faculty]
		return ans	
	if one == '3' and third=='7':
	# сортирует весь фос 3 курс
		df = pd.read_csv('bd/fos_3.csv')
		df = df.sort_values('last_gpa',ascending=True)
		df = df.dropna().reset_index()
		df=df.iloc[::-1]
		# место в общей дб
		d = np.where(df['id']==int(text))
		# по его специальности
		dep = df.loc[df['id'] == int(text)]['department'].values[0]
		
		dep_df = df.loc[df['department'] == dep]
		dep_df = dep_df.sort_values('last_gpa',ascending=True)
		dep_df = dep_df.dropna().reset_index()
		dep_df=dep_df.iloc[::-1]
		# на каком месте он среди специальности цифра
		d =d[0][0]+1
		num = np.where(dep_df['id']==int(text))
		num =num[0][0]+1
		lendth_df=len(df.index)
		lendth_dep=len(dep_df.index)
		faculty = 'Фос 3 курс'
		# ваше место фак, из, название спец,ваше место по спецу ,из,факультет и курс
		ans = [d,lendth_df,dep,num,lendth_dep,faculty]
		return ans	
	if one == '3' and third=='6':
	# сортирует весь фос 4 курс
		df = pd.read_csv('bd/fos_4.csv')
		df = df.sort_values('last_gpa',ascending=True)
		df = df.dropna().reset_index()
		df=df.iloc[::-1]
		# место в общей дб
		d = np.where(df['id']==int(text))
		# по его специальности
		dep = df.loc[df['id'] == int(text)]['department'].values[0]
		
		dep_df = df.loc[df['department'] == dep]
		dep_df = dep_df.sort_values('last_gpa',ascending=True)
		dep_df = dep_df.dropna().reset_index()
		dep_df=dep_df.iloc[::-1]
		# на каком месте он среди специальности цифра
		d =d[0][0]+1
		num = np.where(dep_df['id']==int(text))
		num =num[0][0]+1
		lendth_df=len(df.index)
		lendth_dep=len(dep_df.index)
		faculty = 'Фос 4 курс'
		# ваше место фак, из, название спец,ваше место по спецу ,из,факультет и курс
		ans = [d,lendth_df,dep,num,lendth_dep,faculty]
		return ans
	else:
		return False
		
texta = 4181101
try:
	print(where_my_dep(texta))
except:
	pass
