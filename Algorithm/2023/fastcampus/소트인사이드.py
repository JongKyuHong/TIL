import sys 
input = sys.stdin.readline

N = input().rstrip()
answer = []
for i in N:
    answer.append(i)
print(''.join(sorted(answer, reverse=True)))

