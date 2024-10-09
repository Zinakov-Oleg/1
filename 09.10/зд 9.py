elist=[]
s=0
from random import randint
for i in range (10):
    elist.append(randint(1,100))
for i in range(1):
    print(elist)
for i in elist:
    s+=i
print(s)