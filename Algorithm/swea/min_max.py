t = int(input())
result = []
for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    result.append(max(array)-min(array))
print(*result)



