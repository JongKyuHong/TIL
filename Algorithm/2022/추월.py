import sys
input = sys.stdin.readline

n = int(input())
lst = [] # 입구

for i in range(n):
    lst.append(input().rstrip())
 
lst2 = [] # 출구
for i in range(n):
    lst2.append(input().rstrip())

res = 0
flag = 0
for i in range(n):
    lst_index = lst2.index(lst[i])
    if lst_index < i:
        res += 1
    else:
        tmp = lst[:i]
        tmp2 = []
        cnt = 0
        for j in range(lst_index):
            if lst2[j] in tmp:
                tmp.remove(lst2[j])
        if not tmp:
            continue
        else:
            res += 1
print(res)