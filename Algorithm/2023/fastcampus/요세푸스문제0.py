import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = [i for i in range(1, N+1)]
answer = []
count = 0
idx = 0
while lst:
    count += 1
    if count == K:
        answer.append(lst.pop(idx))
        count = 0
        idx -= 1
    idx += 1
    if lst:
        idx %= len(lst)

print('<' + ', '.join(map(str, answer)) + '>')
    
