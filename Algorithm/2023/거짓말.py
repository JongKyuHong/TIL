import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        if a in lst:
            parent[b] = a
        else:
            parent[a] = b
    else:
        if b in lst:
            parent[a] = b
        else:
            parent[b] = a

N, M = map(int, input().split()) # 사람 수, 파티 수
pp = [0]*(N+1)
lst = list(map(int, input().split()))
lst = lst[1:]
parent = [i for i in range(N+1)]

ans = 0
result = []
for _ in range(M):1
    input_ = list(input().rstrip().split())
    people_cnt, people = input_[0], input_[1:]
    people.sort()
    result.append(people)
    flag = 0
    for i in range(len(people)-1):
        if find(int(people[i])) != find(int(people[i+1])):
            union(int(people[i]), int(people[i+1]))
    if find(int(people[0])) != find(int(people[-1])):
        union(int(people[0]), int(people[-1]))
for people in result:
    flag = 0
    for i in range(len(people)-1):
        if find(int(people[i])) != find(int(people[i+1])):
            union(int(people[i]), int(people[i+1]))
    if find(int(people[0])) != find(int(people[-1])):
        union(int(people[0]), int(people[-1]))
    for p in people:
        p = int(p)
        if parent[p] in lst:
            flag = 1
            break
    if not flag:
        ans += 1
print(ans)