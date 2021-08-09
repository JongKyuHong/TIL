import itertools

n,m,k = map(int,input().split())

def check(array):
    length = len(array)
    dp = [1 for i in range(length)]

    for i in range(length):
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[i],dp[j] + 1)
    if max(dp) == m:
        return True
    else:
        return False
# print(max(dp))
def check2(array):
    length = len(array)
    dp = [1 for i in range(length)]

    for i in range(length):
        for j in range(i):
            if array[i] < array[j]:
                dp[i] = max(dp[i],dp[j] + 1)
    if max(dp) == k:
        return True
    else:
        return False

array = [i for i in range(1,n+1)]
array = list(itertools.permutations(array))
print(len(array))
exit(0)
for i in array:
    if check(i):
        if check2(i):
            print(*i)
            exit(0)
print(-1)


