import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
operator = list(map(int, input().split()))
min_v, max_v = float('inf'), -1*float('inf')
def dfs(val, plus, minus, mul, div, i):
    if i == n:
        global min_v, max_v
        min_v = min(min_v, val)
        max_v = max(max_v, val)
        return
    if plus:
        dfs(val+lst[i], plus-1, minus, mul, div, i+1)
    if minus:
        dfs(val-lst[i], plus, minus-1, mul, div, i+1)
    if mul:
        dfs(val*lst[i], plus, minus, mul-1, div, i+1)
    if div:
        if val < 0 and lst[i] > 0:
            dfs(-1*(abs(val)//lst[i]), plus, minus, mul, div-1, i+1)
        else:
            dfs(val//lst[i], plus, minus, mul, div-1, i+1)

dfs(lst[0], operator[0],operator[1],operator[2],operator[3], 1)
print(max_v)
print(min_v)