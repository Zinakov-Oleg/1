a=int(input("Введите число:"))
if a==0:
    print("Ноль")
elif a<0 and a%2:
    print("Отрицительное нечётное число")
elif a > 0 and a % 2:
    print("Положительное нечётное число")
elif a>0 and a//2:
    print("Положительное чётное чилсо")
elif a<0 and a//2:
    print("Отрицательное чётное число")
else:
    print("ERROR")