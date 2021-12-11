import itertools as it

t = int(input())

for test_case in range(1,t+1):
    n,k = map(int,input().split())
    array = [i for i in range(1,13)]
    result = it.combinations(array,n)
    cnt = 0
    for i in result:
        if sum(i) == k:
            cnt += 1
    print(f'#{test_case} {cnt}')

