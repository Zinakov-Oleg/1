a=int(input("введите цену:"))
b=int(input("введите скидку:"))
c=int(input("введите количество товаров:"))
g=int(input("введите колличество денег:"))
f=0
s=0
for i in range(1, c+1):
    f=(a-(a*(b*i)/100))
    s+=f
    if s>0:
        print(g-s)