import sys

input = sys.stdin.readline

# 1부터 n까지 자연수중에서 m개를 고른 수열
# 같은수 골라도 상관없음
n, m = map(int, input().split())
lst = []

def dfs(cnt, v):
    if cnt - 1 == m:
        print(' '.join(map(str,lst)))
        return
    
    for i in range(1, n+1):
        if i not in lst and i > v:
            lst.append(i)
            dfs(cnt+1, i)
            lst.pop()
dfs(1, 0)