#coding=utf-8
while 1:
    english=input('请输入英文:')
    if english.isalpha() and english!='' :
    	break
    else:
    	print('请重新输入')
if english in ['A','E','I','O','U','a','e','i','o','u'] :
	print('输入的字母为元音')
	print(english+'ay')
else:
	print('输入的是辅音'+english[1:]+english[0]+'ay')
