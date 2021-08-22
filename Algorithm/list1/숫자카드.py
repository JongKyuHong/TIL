t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    ai = input()
    res =[0]*10
    res[0] = -1
    for i in ai:
        res[int(i)] += 1
    res.reverse()
    print(res)
    print(f'#{test_case}',res.index(max(res)),max(res))
