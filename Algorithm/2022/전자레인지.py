import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
time = 0

while A != B:
    if A < 0:
        A += 1
        time += C
    elif A > 0:
        A += 1
        time += E
    else:
        time += D
        A += 1
        time += E
print(time)