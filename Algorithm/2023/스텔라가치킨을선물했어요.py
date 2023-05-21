import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append([a, b])
lst.sort(key=lambda x:x[1])
lst.sort(key=lambda x:x[0], reverse=True)
idx = 5
sol_cnt = lst[4][0]
penalty = lst[4][1]
ans = 0
while idx < len(lst):
    cnt, p = lst[idx][0], lst[idx][1]
    if cnt == sol_cnt:
        ans += 1
        idx += 1
    else:
        break
print(ans)
    

