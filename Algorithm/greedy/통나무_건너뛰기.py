t = int(input())
result = []
for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    array.sort()
    array2= []
    result = 0
    for i in range(2,n):
        result = max(result,abs(array[i]-array[i-2]))
    print(result)
