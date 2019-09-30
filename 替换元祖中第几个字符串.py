#coding=utf-8
str1='who is you father,is this your father?'

def sub1(string,target,num,new):
    g=-1
    b=0
    d=''
    if string.find(target)>0 :
        c=string.partition(target)
        e=c
        while 1 :
            if e[-1].find(target)>0:
                e=e[:-1]+e[-1].partition(target)
            else:
                break
        for m in e:
            g=g+1
            if m==target :
                b=b+1
                if b==num:
                    break
        i=list(e)
        i[g]=new
        for m in i:
            d=d+m
        return d
b=sub1(str1,'is',2,'1')
print(b)
