import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    X = input().rstrip().split()
    x = ''
    for i in X:
        x += i
    x = int(x)

    Y = input().rstrip().split()
    y = ''
    for i in Y:
        y += i
    y = int(y)
    state = list(map(int, input().split()))
    state += state[:m-1]
    idx = 0
    ans = 0
    while idx <= len(state)-m:
        target = ''
        for i in state[idx:idx+m]:
            target += str(i)
        if x <= int(target) <= y:
            ans += 1
        idx += 1
    print(ans)
