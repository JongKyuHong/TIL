t = int(input())

answers = []
result = 0

for _ in range(t):
    arr = []
    n = int(input())
    start = list(input())
    goal = list(input())
    for i in range(n):
        if start[i] != goal[i]:
            arr.append(start[i])
    if arr.count('B') >=arr.count('W'):
        result = arr.count('B')
    else:
        result = arr.count('W')
    answers.append(result)
for answer in answers:
    print(answer)