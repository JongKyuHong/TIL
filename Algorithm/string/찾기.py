import sys

def kmptable(p):
    n = len(p)
    table = [0] * n
    j = 0
    for i in range(1,n):
        while j > 0 and p[i] != p[j]:
            j = table[j-1]
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table


def kmp(s,p):
    j = 0
    cnt = 0
    pos = []
    for i in range(len(s)):
        while j>0 and s[i] != p[j]:
            j = table[j-1]
        if s[i] == p[j]:
            j += 1
            if j == len(p):
                cnt += 1
                pos.append(i-len(p) + 2)
                j = table[j-1]
    return cnt, pos

s = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()
table = kmptable(p)

cnt, pos = kmp(s,p)
print(cnt)
print(*pos)