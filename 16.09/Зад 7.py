a=int(input("Введите координату x 1-ой клетки:"))
b=int(input("Введите координату y 1-ой клетки:"))
c=int(input("Введите координату x 2-ой клетки:"))
d=int(input("Введите координату y 2-ой клетки:"))
if  (a+b)-(c+d)==3 or (c+d)-(a+b)==3:
    print("YES")
elif 0>a>9 or 0>b>9 or 0>c>9 or 0>d>9:
         print("Ошибка!")
else:
    print("NO")