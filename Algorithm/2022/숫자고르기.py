import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
for i in range(n):
    arr.append(int(input()))
answer = set()

def dfs(first, second, num):
    first.add(num)
    second.add(num)
    if arr[num] in first:
        if first == second:
            answer.update(first)
            return 1
        return 0
    return dfs(first, second, arr[num])

for i in range(1, n+1):
    if i not in answer:
        dfs(set(), set(), i)