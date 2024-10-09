b=0
from random import randint
elist=[]
for i in range(100):
    elist.append(randint(0,100000))
for i in elist:
    if i-1<i and i+1<i:
        print(elist.find(i))