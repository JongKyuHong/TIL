import sys
input = sys.stdin.readline

S, C = map(int, input().split())
lst = []
for _ in range(S):
    length = int(input())
    lst.append(length)

ans = 0
left, right = 0, sum(lst)//S
target_v = 0
while left <= right:
    val = 0
    cnt = 0
    target = (left+right)//2
    for i in range(S):
        lst_value = lst[i]
        while lst_value >= target and cnt < C:
            cnt += 1
            lst_value -= target
        val += lst_value
    if cnt == C:
        if target_v < target:
            target_v = target
            ans = val
        left = target + 1
    else:
        right = target - 1
print(ans)