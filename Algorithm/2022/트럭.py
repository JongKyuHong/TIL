import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
lst = list(map(int, input().split()))

bridge = [0] * w
weight = 0
time = 0
while 1:
    out = bridge.pop(0)
    weight -= out

    if lst:
        if weight + lst[0] <= l:
            v = lst.pop(0)
            bridge.append(v)
            weight += v
        else:
            bridge.append(0)
    time += 1
    if not bridge:
        break
    
print(time)