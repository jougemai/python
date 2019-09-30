#coding=utf-8
while True:
	MI_Narcissistic=int(input('请输入一个三位数:'))
	if MI_Narcissistic-999>0 or MI_Narcissistic-99<0 :
		print('格式不正确,请重新输入!')
	else:
		break
hun=MI_Narcissistic//100
decade=(MI_Narcissistic-hun*100)//10
unit=(MI_Narcissistic-hun*100-decade*10)

if (hun**3+decade**3+unit**3)==MI_Narcissistic :
	print('这是一个水仙花数.')
else:
	print('这不是一个水仙花数.')