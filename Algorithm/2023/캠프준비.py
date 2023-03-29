import sys
input = sys.stdin.readline

def solution(idx, sum_v, max_v, min_v):
    if idx == N:
        if sum_v < L or sum_v > R or max_v - min_v < X:
            return
        global ans
        ans += 1
        return
    
    visited[idx] = 1
    m_v, mi_v = max(max_v, lst[idx]), min(min_v, lst[idx])
    solution(idx+1, sum_v + lst[idx], m_v, mi_v)

    visited[idx] = 0
    solution(idx+1, sum_v, max_v, min_v)

N, L, R, X = map(int, input().split())
ans = 0
lst = list(map(int, input().split()))
visited = [0]*N
solution(0, 0, 0, float('inf'))
print(ans)