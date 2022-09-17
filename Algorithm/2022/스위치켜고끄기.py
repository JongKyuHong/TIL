import sys
input = sys.stdin.readline

N = int(input())
switch = [0] + list(map(int, input().split()))

M = int(input())
students = [map(int, input().split()) for _ in range(M)]

for s, idx in students:
    if s == 1:
        for i in range(idx, N+1):
            if i % idx == 0:
                switch[i] = abs(switch[i]-1)
    else:
        left = idx - 1
        right = idx + 1
        switch[idx] = abs(switch[idx]-1)
        while 1:
            if 1 <= left and right < N+1:
                if switch[left] == switch[right]:
                    switch[left] = abs(switch[left]-1)
                    switch[right] = abs(switch[right]-1)
                    left -= 1
                    right += 1
                else:
                    break
            else:
                break

switch = switch[1:]
v = 0
for i in switch:
    v += 1
    if v == 20:
        print(i)
        v = 0
    else:
        print(i, end=' ')
    