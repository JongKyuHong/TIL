for T in range(int(input())):
    n, m = map(int, input().split()) # A의 단어 갯수, B의 단어 갯수
    A = [list(input()) for _ in range(n)]
    B = [list(input()) for _ in range(m)]
    cnt = 0
    for a in A:
        if a in B:
            cnt += 1
    print(f'#{T+1} {cnt}')