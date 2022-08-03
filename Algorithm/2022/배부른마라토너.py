n = int(input())
names = [input() for _ in range(n)]
names2= [input() for _ in range(n-1)]

for i in names:
    if i not in names2:
        print(i)