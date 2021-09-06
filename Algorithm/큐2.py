from collections import deque
queue = deque([])
for _ in range(int(input())):
    a = list(input().split())
    print(a[0])
    if a[0] == 'push':
        queue.append(a[-1])
    elif a[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print('-1')
    elif a[0] == 'size':
        print(len(queue))
    elif a[0] == 'empty':
        if queue:
            print('0')
        else:
            print('1')
    elif a[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print('-1')
    else:
        if queue:
            print(queue[-1])
        else:
            print('-1')
