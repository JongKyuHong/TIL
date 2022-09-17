for T in range(int(input())):
    n, m = map(int, input().split()) # A의 단어 갯수, B의 단어 갯수
    A = [input() for _ in range(n)]
    B = [input() for _ in range(m)]
    res = 0
    for b in B:
        flag = 0
        for a in A:
            if a.startswith(b):
                flag = 1
                break
        if flag:
            res += 1
    print(f'#{T+1} {res}')