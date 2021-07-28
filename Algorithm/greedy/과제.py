n = int(input())
array = []
for _ in range(n):
    d,w = map(int,input().split())
    array.append([d,w])
array1 = sorted(array,key=lambda x: (x[0],x[1]),reverse=True)
dead = array1[0][0]
result = array1[0][1]
count = 0
i = 1
while d > 0:
    if d <= array[i][0]:
        for j in range(i,len(array1)):
            count = max(count, array[i][1])
        print(count)
        result += count
        d -= 1
    else:
        d -= 1
print(result)
