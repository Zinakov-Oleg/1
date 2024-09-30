a=int(input("Введите начальный член a:"))
n=int(input("Введите кол-во чисел:"))
r=int(input("Введите знаменатель:"))
for i in range(1, n+1):
    f=a*r**(i-1)
    print(f)