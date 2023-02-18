from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
dic = defaultdict(int)
for _ in range(N):
    e, x = map(int, input().split())
    dic[e] += 1
    dic[x] -= 1

tem, txm = 0, 0
cnt, max_v = 0, 0
for k, v in sorted(dic.items()):
    cnt += v
    if cnt > max_v:
        max_v = cnt
        tem = k
        flag = True
    elif cnt < max_v and flag and cnt - v == max_v:
        txm = k
        flag = False

print(tem, txm)
        

        

