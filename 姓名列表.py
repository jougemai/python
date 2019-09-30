#coding=utf-8
list1=[]
while 1:
	name=input('请输入一个名字')
	if len(name)!=0:
		if name in list1 :
			print('已存在该姓名')
		else:
			list1.append(name)
			print(name)
	else:
		print('输入不能为空')
