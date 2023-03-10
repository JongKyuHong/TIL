import sys
input = sys.stdin.readline

T = int(input())
def check(inp, mid):
    for i in range(mid):
        if inp[i] == inp[mid*2-i]:
            return 0
    return 1

def solution(inp):
    if len(inp) == 1:
        return 1
    mid = len(inp) // 2
    return check(inp, mid) and solution(inp[:mid]) and solution(inp[mid+1:])

for _ in range(T):
    inp = input().rstrip()
    if solution(inp):
        print("YES")
    else:
        print("NO")
