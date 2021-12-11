def dfs(idx):
    global charge, result

    if idx >= len(lst):
        if result >= charge:
            result = charge
        return

    if result <= charge:
        return

    for i in range(idx+lst[idx], idx, -1):
        charge += 1
        dfs(i)
        charge -= 1


T = int(input())

for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    result = 987654321  # 현재까지의 최소 값
    charge = 0  # 지금까지 충전 횟수
    dfs(1)

    print(f'#{test_case} {result-1}')