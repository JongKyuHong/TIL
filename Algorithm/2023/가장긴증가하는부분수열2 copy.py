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
ans = [lst[0]]
for i in range(1, N):
    if ans[-1] > lst[i]:
        idx = find(len(ans), lst[i])
        ans[idx] = lst[i]
    elif ans[-1] < lst[i]:
        ans.append(lst[i])
print(len(ans))
