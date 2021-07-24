t = int(input())
money = [25,10,5,1]
for _ in range(t):
    c = int(input())
    for i in range(4):
        print(c // money[i],end=' ')
        c %= money[i]
    print()


