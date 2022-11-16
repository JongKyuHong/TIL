import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
#visited = [[0]*n for _ in range(n)]
delta = ((0,1),(1,0))
res = 0

answer = 0

for i in range(n):
    value = graph[0][i]
    answer = 1
    for j in range(1, n):
        if value == graph[j][i]:
            answer += 1
        else:
            res = max(res, answer)
            answer = 1
            value = graph[j][i]
    res = max(res, answer)


for i in range(n):
    value = graph[i][0]
    answer = 1
    for j in range(1, n):
        if value == graph[i][j]:
            answer += 1
        else:
            res = max(res, answer)
            answer = 1
            value = graph[i][j]
    res = max(res, answer)


for i in range(n):
    for j in range(n):
        target = graph[i][j]
        for k in range(2):
            if k == 0: # 오른쪽이랑 비교
                r, c = i, j
                c += 1
                if 0 <= c < n:
                    if target != graph[r][c]:
                        tmp = graph[r][c]
                        graph[r][c] = graph[i][j]
                        graph[i][j] = tmp
                        
                        value = graph[0][c]
                        answer = 1
                        for a in range(1, n):
                            if value == graph[a][c]:
                                answer += 1
                            else:
                                res = max(res, answer)
                                answer = 1
                                value = graph[a][c]
                        
                        res = max(res, answer)

                        value = graph[0][j]
                        answer = 1
                        for a in range(1, n):
                            if value == graph[a][j]:
                                answer += 1
                            else:
                                res = max(res, answer)
                                answer = 1
                                value = graph[a][j]
                        res = max(res, answer)

                        value = graph[i][0]
                        answer = 1
                        for a in range(1, n):
                            if value == graph[i][a]:
                                answer += 1
                            else:
                                res = max(res, answer)
                                answer = 1
                                value = graph[i][a]
                        res = max(res, answer)

                        value = graph[r][0]
                        answer = 1
                        for a in range(1, n):
                            if value == graph[r][a]:
                                answer += 1
                            else:
                                res = max(res, answer)
                                answer = 1
                                value = graph[r][a]
                        res = max(res, answer)

                        tmp = graph[r][c]
                        graph[r][c] = graph[i][j]
                        graph[i][j] = tmp
            else:
                r, c = i, j
                r += 1
                if 0 <= r < n:
                    if target != graph[r][c]:
                        tmp = graph[r][c]
                        graph[r][c] = graph[i][j]
                        graph[i][j] = tmp
                        
                        value = graph[0][c]
                        answer = 1
                        for a in range(1, n):
                            if value == graph[a][c]:
                                answer += 1
                            else:
                                res = max(res, answer)
                                answer = 1
                                value = graph[a][c]
                        res = max(res, answer)

                        value = graph[0][j]
                        answer = 1
                        for a in range(1, n):
                            if value == graph[a][j]:
                                answer += 1
                            else:
                                res = max(res, answer)
                                answer = 1
                                value = graph[a][j]
                        res = max(res, answer)

                        value = graph[i][0]
                        answer = 1
                        for a in range(1, n):
                            if value == graph[i][a]:
                                answer += 1
                            else:
                                res = max(res, answer)
                                answer = 1
                                value = graph[i][a]
                        res = max(res, answer)

                        value = graph[r][0]
                        answer = 1
                        for a in range(1,n):
                            if value == graph[r][a]:
                                answer += 1
                            else:
                                res = max(res, answer)
                                answer = 1
                                value = graph[r][a]
                        res = max(res, answer)

                        tmp = graph[r][c]
                        graph[r][c] = graph[i][j]
                        graph[i][j] = tmp
print(res)