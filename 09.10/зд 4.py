elist=[]
from random import randint
for i in range(10):
    elist.append(randint(1,100))
print(elist)
elist.clear()
print(elist)