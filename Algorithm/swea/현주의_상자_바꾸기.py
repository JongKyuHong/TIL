t = int(input())

for test_case in range(1,t+1):
    n,q = map(int,input().split())
    array = [0]*n
    for i in range(q):
        l,r = map(int,input().split())
        for j in range(l-1,r):
            array[j] = i+1
    print(f'#{test_case}', *array)