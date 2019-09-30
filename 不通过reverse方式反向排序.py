str1='asdf456sxc3245vkvhdlgn123l1'
bb=[a for a in str1]
c=[]
while 1:
    c.append(bb.pop())
    if bb==[] :
        break
print(c)
d=''
for b in c:
    d=d+b
print(d)
