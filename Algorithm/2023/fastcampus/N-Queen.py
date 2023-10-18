import sys 
input = sys.stdin.readline

def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x]-row[i]) == x-i:
            return False
    return True

N = int(input())
answer = 0
def dfs(x):
    if x == N:
        global answer
        answer += 1
    else:
        for i in range(N):
            row[x] = i
            if check(x):
                dfs(x+1)
row = [0]*N
dfs(0)

print(answer)