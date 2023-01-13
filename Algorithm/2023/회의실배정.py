import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x:(x[1],x[0]))

cnt = 0
tmp_end = 0
for start, end in lst:
    if cnt == 0:
        cnt += 1
        tmp_end = end
    else:
        if tmp_end <= start:
            tmp_end = end
            cnt += 1
print(cnt)