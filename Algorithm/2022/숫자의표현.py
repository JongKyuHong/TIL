def solution(n):
    ans = 0
    base = 1
    tmp = base
    cnt = 0
    while base <= n:
        ans += tmp
        tmp += 1
        if ans == n:
            cnt += 1
            ans = 0
            base += 1
            tmp = base
        elif ans > n:
            ans = 0
            base += 1
            tmp = base
    print(cnt)

solution(15)