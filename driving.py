country = input('請輸入您的國家：')
age = input('請輸入您的年齡： ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('您可以考駕照')
	else:
		print('您還不能考駕照')
elif country == '美國':  #根源於if,為if的延伸
	if age >= 16:
		print('您可以考駕照')
	else:
		print('您還不能考駕照')
else:
	print('只能輸入台灣或美國')
country = input('請輸入您的國家：')
age = input('請輸入您的年齡： ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('您可以考駕照')
	else:
		print('您還不能考駕照')
elif country == '美國':  #根源於if,為if的延伸
	if age >= 16:
		print('您可以考駕照')
	else:
		print('您還不能考駕照')
