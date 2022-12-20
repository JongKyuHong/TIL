import sys
input = sys.stdin.readline


s, p = map(int, input().split())
dna = input().rstrip()
min_lst = list(map(int, input().split())) # A C G T
standard = sum(min_lst)

for i in dna[:p]:
    if i == 'A':
        min_lst[0] = min_lst[0] - 1
    elif i == 'C':
        min_lst[1] = min_lst[1] - 1
    elif i == 'G':
        min_lst[2] = min_lst[2] - 1
    else:
        min_lst[3] = min_lst[3] - 1

start = 0
end = p-1
cnt = 0
while 1:
    flag = 0
    for i in min_lst:
        if i > 0:
            flag = 1
    if not flag:
        cnt += 1
    i = dna[start]
    if i == 'A':
        min_lst[0] = min_lst[0] + 1
    elif i == 'C':
        min_lst[1] = min_lst[1] + 1
    elif i == 'G':
        min_lst[2] = min_lst[2] + 1
    else:
        min_lst[3] = min_lst[3] + 1
    start += 1
    end += 1
    if end >= s:
        break
    i = dna[end]
    if i == 'A':
        min_lst[0] = min_lst[0] - 1
    elif i == 'C':
        min_lst[1] = min_lst[1] - 1
    elif i == 'G':
        min_lst[2] = min_lst[2] - 1
    else:
        min_lst[3] = min_lst[3] - 1
print(cnt)