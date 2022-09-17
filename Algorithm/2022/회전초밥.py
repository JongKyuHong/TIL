import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split()) # 접시수, 가짓수, 연속수, 쿠폰번호
N = [int(input()) for _ in range(n)]
flag = 0
if c in N:
    idx = N.index(c)
else:
    flag = 1
summary = {} # idx:1
start = 0
end = k
max_v = 0
for i in range(start,end):
    if N[i%n] in summary:
        summary[N[i%n]] += 1
    else:
        summary[N[i%n]] = 1

#print(summary)
len_summary = len(summary)
if flag == 0:
    if N[idx] not in summary:
        len_summary += 1
else:
    len_summary += 1

max_v = max(max_v, len_summary)

if summary[N[start%n]] - 1 == 0:
    del summary[N[start%n]]
else:
    summary[N[start%n]] -= 1
start += 1
end += 1

while start < n:
    if N[(end-1)%n] in summary:
        summary[N[(end-1)%n]] += 1
    else:
        summary[N[(end-1)%n]] = 1
    len_summary = len(summary)
    #print(summary,start,end,'summary')
    if flag == 0:
        if N[idx] not in summary:
            len_summary += 1
    else:
        len_summary += 1
    
    max_v = max(max_v, len_summary)
    if summary[N[start%n]] - 1 == 0:
        del summary[N[start%n]]
    else:
        summary[N[start%n]] -= 1
    start += 1
    end += 1
print(max_v)

