import sys
input = sys.stdin.readline

n = int(input())
answer = ''
while n > 0:
    n, r = divmod(n, 2)
    answer += str(r)

print(int(answer, 2))

