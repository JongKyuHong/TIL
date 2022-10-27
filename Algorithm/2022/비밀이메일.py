import sys 
input = sys.stdin.readline

my_str = input().rstrip()
r = 1
c = len(my_str)

for i in range(1,len(my_str)+1):
    if len(my_str) % i == 0:
        if r < i and i <= len(my_str) // i:
            r = i
            c = len(my_str) // i

d = [[] for _ in range(r)]
cnt = 0

for i in range(c):
    for k in range(r):
        d[k].append(my_str[cnt])
        cnt += 1

for i in range(r):
    print(''.join(d[i]),end='')
