n=int(input("Введите число:"))
if n<=100 or n>999:
       print("Число должно быть от 100 до 1000")
else:
    for i in range(100, n):
        n1=i//100%10
        n2=i//10%10
        n3=i%10
        if n1==n3:
         print(i)
        else:
            pass