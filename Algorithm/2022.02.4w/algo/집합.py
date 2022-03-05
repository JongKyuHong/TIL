m = int(input())
array = []
for _ in range(m):
    t = list(input().split())
    print(t)
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