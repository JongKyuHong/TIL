import sys
import copy
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
ans = 0

def makemax(val, q):
    global ans
    if len(q) == 2:
        ans = max(ans, val)
        return
    for i in range(1, len(q)-1):
        val2 = q[i-1]*q[i+1]
        tmp = q.pop(i)
        makemax(val+val2, q)
        q.insert(i, tmp)

makemax(0, lst)
print(ans)