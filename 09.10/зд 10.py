elist=[]
s=0
r=0
d=0
from random import randint
for i in range (10):
    elist.append(randint(1,10))
print(elist)
for i in elist:
    s+=i
    d=len(elist)
    r=s/d
print(r)