#coding=utf-8
def tran_dict(path):
	with open(path,'r') as file1:
		file2=file1.read()
	c=[]
	for a in file2.strip("'"):
		if a!="'":
			c.append(a)
	del c[0]
	del c[-1]
	b=''
	for a in c :
		b=b+a
	dict1={}
	for d in b.split(','):
		g=d.partition(':')
		dict1[g[0]]=g[2]
	return dict1
c=tran_dict('D:\\2.txt')
print(c)
