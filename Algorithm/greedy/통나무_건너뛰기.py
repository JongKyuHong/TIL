t = int(input())
result = []
for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    array.sort(reverse=True)
    result = max(array[0]-array[1],array[0]-array[2])
    print(result)

