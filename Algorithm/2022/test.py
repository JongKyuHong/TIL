n, m = map(int, input().split())
choose = [0 for _ in range(10)]
used = [0 for _ in range(10)]


def dfs(cnt):
    global n, m
    if cnt == m:
        for idx in range(cnt):
            print(choose[idx], end=' ')
        print()
        return
    for i in range(1, n+1):
        if used[i]:
            continue
        used[i] = 1
        choose[cnt] = i
        dfs(cnt + 1)
        used[i] = 0

dfs(0)