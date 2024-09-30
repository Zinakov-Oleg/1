n=int(input("Введите кол-во участков:"))
x=0
z=0
t=0
m=0
l=0
s=0
for i in range(1, n+1):
    s=int(input("Введите расстояние(в км):"))
    x+=s
    v=int(input("Введите среднюю скорость(км/ч):"))
    z+=v
    t=s//v
    l+=t
print(f"Общее время {l}")