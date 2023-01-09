import sys
input = sys.stdin.readline

N = int(input())
lst = [0]*N
answers = [0]*N
people = []
for _ in range(N):
    P, Q = map(int, input().split())
    people.append([P,Q])
people.sort()

for person in people:
    for i in range(N):
        if lst[i] <= person[0]:
            lst[i] = person[1]
            answers[i] += 1
            break

idx = N
for i in range(N):
    if answers[i] == 0:
        idx = i
        break
print(len(answers[:idx]))
print(*answers[:idx])