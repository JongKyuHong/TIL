n = int(input()) 
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
array = sorted(array,key=lambda x: (x[1],x[0]))
ans = end= 0
for s,e in array:
    if s >= end:
        ans += 1
        end = e
print(ans)


## 다돌아서 시간 오류