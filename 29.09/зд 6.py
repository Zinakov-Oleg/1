p=int(input("Введите население на данный момент:"))
r=int(input("Введите прирост в год:"))
n=int(input("Через сколько лет:"))
for i in range(n+1):
    print(int(p * ((1 + r / 100) ** i)))