n,l,k = map(int,input().split())
array = []
for _ in range(n):
    sub1, sub2 = map(int,input().split())
    array.append([sub1,sub2])

array.sort(key=lambda x:(x[1]))
print(array)
cnt = 0
while k > 0 and array:
    sub1, sub2 = array.pop(0)
    if sub2 <= l:
        cnt += 140
        k -= 1
    elif sub1 <= l:
        cnt += 100
        k -= 1

print(cnt)

