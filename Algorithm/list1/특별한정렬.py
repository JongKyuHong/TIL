t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    ai = list(map(int,input().split()))
    ai.sort()
    res = []
    for i in range(1,(len(ai)//2)+1):
        res.append(ai[-i])
        res.append(ai[i-1])
    res = res[:10]
    print(f'#{test_case}', *res)






