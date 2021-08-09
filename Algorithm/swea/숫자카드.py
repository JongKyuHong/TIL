t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    text = list(input())
    maxa = 0
    result = []
    for i in set(text):
        if maxa<=text.count(i):
            result.append([int(i),text.count(i)])
    result.sort(key=lambda x:(x[1],x[0]))
    a = result[-1][0]
    b = result[-1][-1]
    print(f'#{test_case} {a} {b}')


