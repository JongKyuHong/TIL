import sys
input = sys.stdin.readline

N = int(input())
for i in range(1,N+1):
    inp = input().rstrip()
    print(f'{i}. {inp}')
