n = int(input())
k = int(input())
array = list(map(int,input().split()))
array.sort()
result = []
if k>=n:
    print(0)
else:
    for i in range(len(array)-1):
        result.append(abs(array[i]-array[i+1]))
    result.sort(reverse=True)
    answer = sum(result)
    for i in range(k-1):
        answer -= result[i]
    print(answer)