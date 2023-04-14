import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst_set = set(lst)
max_v = 1
for s in lst_set:
    prev = s
    prev_cnt = 1
    for l in lst:
        if l == s:
            continue
        else:
            if prev == l:
                prev_cnt += 1
            else:
                max_v = max(max_v, prev_cnt)
                prev = l
                prev_cnt = 1
    max_v = max(max_v, prev_cnt)
print(max_v)