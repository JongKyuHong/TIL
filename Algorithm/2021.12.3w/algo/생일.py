n = int(input())
array = []
for _ in range(n):
    n,d,m,y = input().split()
    array.append((n,int(d),int(m),int(y)))
array.sort(key=lambda x: (x[3],x[2],x[1]))
print(array[-1][0])
print(array[0][0])