import sys
input = sys.stdin.readline

N = input().rstrip()
n = len(N)
target = n*(n+1)//2
answer = set()

def dfs(left, right, string):
    if len(string) == target:
        answer.add(string)
        return
    if left > 0:
        dfs(left-1, right, string+N[left-1:right+1])
    if right < n:
        dfs(left, right+1, string+N[left:right+2])
    

for i in range(n):
    dfs(i, i, N[i])
print(len(answer))