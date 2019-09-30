#coding=utf-8
str1='who is you father'
'''
def sub(insert,taget,new):
	dict={}
	for m in insert:
		dict[m]=insert.find(taget)
	print(dict)
a=sub()
a(str1,' ',b)
def sub1(string,target,num,new):
    m=0
    b=0
    for mid in string :
        if mid==target :
            b=b+1
        m=m+1
        if b==num:
            break
            '''
def sub1(string,target,num,new):
    b=0
    d=''
    if string.find(target)>0 :
        print(1)
        c=string.partition(target)
        e=c
        while 1 :
            if e[-1].find(target)>0:
                print(2)
                e=e[:-1]+e[-1].partition(target)
            else:
                print(3)
                break
        print(e)
        for m in e:
            if m==target :
                b=b+1
                if b==num:
                    print(type(b))
                    break
        e[b]=new
        for m in e:
            d=d+m
        return d
b=sub1(str1,' ',2,'1')
    
    
