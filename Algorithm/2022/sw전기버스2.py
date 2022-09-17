def dfs(idx, _sum):
    global answer
    if idx >= n-1:
        answer = min(answer, _sum)
        return
    if _sum > answer:
        return
    charge = lst[idx]
    for i in range(charge, 0, -1):
        dfs(idx+i, _sum + 1)

for T in range(int(input())):
    data = list(map(int, input().split()))
    n = data[0]
    lst = data[1:]
    answer = float('inf')
    dfs(0, -1)
    print(f'#{T+1} {answer}')
