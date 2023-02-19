import sys
input = sys.stdin.readline

k = int(input())
lst = list(input().rstrip().split())

nums = [0,1,2,3,4,5,6,7,8,9]
cnt1 = 0
cnt2 = 0
for i in lst:
    if i == '<':
        cnt1 += 1
    else:
        cnt2 += 1

max_v = 0
max_str = ''
min_v = float('inf')
min_str = ''
def dfs(num, idx, cnt11, cnt22):
    if idx == k:
        global max_v, min_v, max_str, min_str
        if max_v < int(num):
            max_v = int(num)
            max_str = num
        if min_v > int(num):
            min_v = int(num)
            min_str = num
        return
    if lst[idx] == '<':
        if int(num[-1])+k >= 10:
            for j in range(int(num[-1])+1, 10):
                if str(j) not in num:
                    dfs(num+str(j), idx+1, cnt11-1, cnt22)
        else:
            for j in range(int(num[-1])+1, int(num[-1])+k+1):
                if str(j) not in num:
                    dfs(num+str(j), idx+1, cnt11-1, cnt22)
    elif lst[idx] == '>':
        if int(num[-1])-k <= 0:
            for j in range(0, int(num[-1])):
                if str(j) not in num:
                    dfs(num+str(j), idx+1, cnt11, cnt22-1)
        else:
            for j in range(int(num[-1])-k, int(num[-1])):
                if str(j) not in num:
                    dfs(num+str(j), idx+1, cnt11, cnt22-1)

for i in range(10):
    dfs(str(i), 0, cnt1, cnt2)
print(max_str)
print(min_str)
