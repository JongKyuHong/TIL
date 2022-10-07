import sys
input = sys.stdin.readline

A, P = map(int, input().split())
o_dict = {A:1}
idx = 0
while idx <= 9999:
    idx += 1
    A = str(A)
    target = 0
    for i in A:
        target += int(i)**P
    if target not in o_dict:
        o_dict[target] = 1
    else:
        o_dict[target] += 1
    A = target
cnt = 0
for k, v in o_dict.items():
    if v == 1:
        cnt += 1
print(cnt)