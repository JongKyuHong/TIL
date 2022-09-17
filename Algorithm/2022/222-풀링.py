import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

def solution(x, y, N):
    if N == 2:
        res = []
        for i in range(x, x+N):
            for j in range(y, y+N):
                res.append(graph[i][j])
        res.sort()
        return res[-2]
    s1 = solution(x, y, N//2)
    s2 = solution(x, y+N//2, N//2)
    s3 = solution(x+N//2, y, N//2)
    s4 = solution(x+N//2, y+N//2, N//2)
    answer = [s1,s2,s3,s4]
    answer.sort()
    return answer[-2]

print(solution(0, 0, N))