n = list(map(int,input()))
n.sort(reverse=True)
a = ''
for i in n:
    a += str(i)
a = int(a)
if a % 30 == 0:
    print(a)
else:
    print(-1)