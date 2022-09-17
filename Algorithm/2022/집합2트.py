import sys
input = sys.stdin.readline

s = set()
M = int(input())
for _ in range(M):
    tmp = input().rstrip().split()
    if len(tmp) == 1:
        if tmp[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue
    
    command, target = tmp[0], tmp[1]
    target = int(target)

    if command == 'add':
        s.add(target)
    elif command == 'check':
        print(1 if target in s else 0)
    elif command == 'remove':
        s.discard(target)
    elif command == 'toggle':
        if target in s:
            s.discard(target)
        else:
            s.add(target)
