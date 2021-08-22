t = int(input())

def check(n, k):
    for i in range(1<<12):
        subset = []
        sum_v = 0
        for j in range(12):
            if i & (1<<j):
                subset.append(a[j])
                sum_v += a[j]
        if len(subset) == n and sum_v == k:
            return 1
    return 0


for test_case in range(1,t+1):
    n, k = map(int,input().split())
    a = list(range(1,13))
    print(f'#{test_case}', check(n,k))





