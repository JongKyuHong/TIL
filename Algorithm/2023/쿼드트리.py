import sys
input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
answer = ''

def divide(r, c, n):
    global answer
    if n == 1:
        answer += str(graph[r][c])
        return
    standard = graph[r][c]
    flag = 0
    for i in range(r, r+n):
        for j in range(c, c+n):
            if graph[i][j] != standard:
                flag = 1
                answer += '('
                divide(r, c, n//2)
                divide(r, c+n//2, n//2)
                divide(r+n//2, c, n//2)
                divide(r+n//2,c+n//2, n//2)
                answer += ')'
                break
        if flag:
            break
    if not flag:
        answer += str(standard)
        
divide(0, 0, N)
print(answer)