<<<<<<< HEAD
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
=======
m = int(input())
array = []
for _ in range(m):
    t = list(input().split())
    if len(t) == 2:
        if t[0] == 'add':
            array.append(t[1])
        elif t[0] == 'check':
            if t[1] in array:
                print(1)
            else:
                print(0)
        elif t[0] == 'remove':
            if t[1] in array:
                array.remove(t[1])
        elif t[0] == 'toggle':
            if t[1] in array:
                array.remove(t[1])
            else:
                array.append(t[1])
    else:
        if t == 'all':
            array = [i for i in range(20)]
        else:
            array = []
>>>>>>> 6f6784b1e7f5e08d85fdb3f1fc44bf9704170fd0
