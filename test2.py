#coding=utf-8
m=0
while 1:
	b=input('显示多少行星号:')
	if len(b)!=0:
		m=int(b)
		break
	else:
		print('请重新输入')
for i in range(-m,m):
    if i<0:
        print((abs(i+1)*" ")+((2*(i+(m+1))-1)*"*"))
    if i>=1:
        print(i*" "+((2*m-1)-(2*i))*"*")
        '''
   *
  ***
 *****
*******
'''
