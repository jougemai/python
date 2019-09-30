#coding=utf-8
while True:
	year=int(input('请输入一个四位数的年份'))
	if year//10000>0 or year//1000==0 :
		print('请输入一个正确的四位数的年份')
	else:
		break
if year%4==0 and year%100>0 :
	print('是个闰年')
else:
	print('不是个闰年')
