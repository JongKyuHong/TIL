n = int(input())
a = list(map(int,input().split()))
d = [0]*23
for i in a:
    d[i-1] += 1
for i in d:
    print(i,end=' ')