n = int(input())
lista = list(map(int, input().split()))

q = int(input())
listq = list(map(int, input().split()))

result = []
for i in range(q):
    start, end = 0, n-1
    target = listq[i]
    check = 1
    while start <= end:
        mid = (start+end)//2
        if lista[mid] == target:
            result.append(mid)
            check = 0
            break
        elif lista[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    if check:
        result.append(-1)

for i in result:
    print(i, end=' ')

