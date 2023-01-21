import sys
input = sys.stdin.readline

def find(len_ans, target):
    if len_ans == 1:
        return 0
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
n = int(input())
lst = list(map(int, input().split()))
if n == 1:
    print(1)
    exit()
ans = [lst[0]]
for i in range(1, n):
    if ans[-1] > lst[i]:
        idx = find(len(ans), lst[i])
        ans[idx] = lst[i]
    else:
        ans.append(lst[i])

print(len(ans))