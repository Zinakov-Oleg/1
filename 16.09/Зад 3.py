a=int(input("Введите число:"))
b=int(input("Введите число:"))
c=int(input("Введите число:"))
if a>0 and b>0 and c>0:
    if a+b>c and b+c>a and c+a>b:
        print("YES")
    else:
         print("NO")