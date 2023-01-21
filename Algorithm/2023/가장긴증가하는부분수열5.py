import sys
input = sys.stdin.readline

def find(len_ans, target):
    left, right = 0, len_ans-1
    while left <= right:
        mid = (left+right)//2
        if ans[mid] == target:
            return mid
        elif ans[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left

N = int(input())
lst = list(map(int, input().split()))
ans = []
trace = []
max_idx = 0
for i in range(N):
    if not ans or ans[-1] < lst[i]:
        ans.append(lst[i])
        trace.append(max_idx)
        max_idx += 1
    else:
        idx = find(len(ans), lst[i])
        ans[idx] = lst[i]
        trace.append(idx)
print(trace)
print(ans)
print(len(ans))
max_v = len(ans)-1
path = []
for i in range(N-1, -1, -1):
    if max_v == trace[i]:
        path.append(lst[i])
        max_v -= 1
path.reverse()
print(*path)