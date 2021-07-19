import math

def root(a,b,c):
    con1 = b**2 -4*a*c
    if con1 >= 0:
        x1 = (-b + math.sqrt(con1))/(2*a)
        x2 = (-b - math.sqrt(con1))/(2*a)
    else:
        return -1
    return x1, x2

a,b,c = map(float,input("a ,b ,c 를 입력").split())
while a == 0:
    a = float(input('a를 다시 입력'))
print(a,b,c)
x1 = root(a,b,c)
if x1 == -1:
    print("근이 없다.")
else:
    print(f'근1 : {x1[0]} 근2 : {x1[1]}')

