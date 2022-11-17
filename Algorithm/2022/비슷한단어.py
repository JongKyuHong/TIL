import sys 
input = sys.stdin.readline

def add(idx, r):
    global target 
    for i in range(26):
        res = r[:]
        res.insert(idx, str(chr(65+i)))
        if target == sorted(res):
            return 1
    return 0

def delete(idx, r):
    res = r[:]
    res.pop(idx)
    if target == sorted(res):
        return 1
    return 0

def change(idx, r):
    res = r[:]
    for i in range(26):
        res[idx] = chr(65+i)
        if target == sorted(res):
            return 1
    return 0
n = int(input())
answer = 0
target = []
result = []
for i in range(n):
    data = list(input().rstrip())
    if i == 0:
        target = data
    else:
        result.append(data)

target.sort()
for res in result:
    if target == sorted(res):
        answer += 1
        continue
    flag = 0
    for i in range(len(res)+1):
        if add(i, res):
            answer += 1
            flag = 1
            break
    if flag:
        continue
    for i in range(len(res)):
        if delete(i, res):
            answer += 1
            flag = 1
            break
    if flag:
        continue

    for i in range(len(res)):
        if change(i, res):
            answer += 1
            flag = 1
            break
    if flag:
        continue
    
print(answer)