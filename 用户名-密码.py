import time
dic={'mlsh':'mlsh'}
while 1:
	login_logon=int(input('注册请输入1,已注册请输入0,退出请输入2:'))
	if login_logon==0 :
		while 1:
			logon=input('请输入用户名:')
			num=0
			if logon in dic.keys():
				while 1:
					login=input('请输入密码:')
					if login==dic[logon]:
						print('密码正确')
						break
					else:
						print('密码错误,请重新输入密码')
						with open('D:\\mistakepw','a') as f:
							f.write(time.asctime( time.localtime(time.time()) )+'错误的密码:'+login+'\n')
						num=num+1
					if num==3 :
						print('密码错误次数超过3次')
						break
				break
			else :
				print('用户名不存在')
				with open('D:\\mistakename','a') as f:
					f.write(time.asctime( time.localtime(time.time()) )+'错误的用户名:'+logon+'\n')
		break
	elif login_logon ==1:
		while 1:
			new_name=input('请输入新的用户名')
			if new_name in dic.keys():
				print('该用户名已被注册')
			else:
				break
		new_passwd=input('请输入密码')
		dic[new_name]=new_passwd
	elif login_logon==2:
		break
	else:
		print('请重新输入')
            
            
