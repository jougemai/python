#coding=utf-8
str1='who is you father,is this your father?'

class fun_sub:
	def __init__(self):
		self.string=None
		self.target=None
		self.num=None
		self.new=None
	def sub1(self):
		__sub1_m1=-1
		__sub1_m2=0
		__sub1_m3=''
		__sub1_m4=()
		if self.string.find(self.target)>0 :
			__sub1_m4=self.string.partition(self.target)
			__sub1_m5=__sub1_m4
			while 1:
				if __sub1_m5[-1].find(self.target)>0:
					__sub1_m5=__sub1_m5[:-1]+__sub1_m5[-1].partition(self.target)
				else:
					break
	def sub2(self):
		for __sub2_m1 in __sub1_m5 :
			__sub1_m1=__sub1_m1+1
			if __sub2_m1==self.target :
				__sub1_m2=__sub1_m2+1
				if b==self.num:
					break
		__sub2_m3=list(__sub1_m5)
		__sub2_m3[__sub1_m1]=self.new
		for __sub2_m4 in __sub2_m3:
			__sub1_m3=__sub1_m3+__sub2_m4
		return __sub1_m3

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
