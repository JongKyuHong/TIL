def dfs(cnt):
    if cnt == n:
        if len(a_list) == n//2:
            global res
            b_list = []
            for i in range(n):
                if i not in a_list:
                    b_list.append(i)
            a, b = 0, 0
            for i in a_list:
                for j in a_list:
                    a += array[i][j]
            for i in b_list:
                for j in b_list:
                    b += array[i][j]
            res = min(res, abs(a-b))
        return
    a_list.append(cnt)
    dfs(cnt + 1)
    a_list.remove(cnt)
    dfs(cnt + 1)
for test_case in range(int(input())):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    res = float('inf')
    a_list = []
    dfs(0)
    print(f'#{test_case+1} {res}')