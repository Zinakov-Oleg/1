n=int(input("Введите количество чисел:"))
a=0
b=1
c=0
for i in range(1, n+1):
    a+=i
    print(f"Сумма чисел равна {a}")
    b*=i
    print(f"Произведение чисел равно {b}")
    c=a/n
    print(f"среднее арифметическое равно{c}")
