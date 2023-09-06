import sys 
input = sys.stdin.readline

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0]*W
weight = 0
idx = 0
time = 0
while 1:
    out = bridge.pop(0)
    time += 1
    if idx < N:
        if sum(bridge)+trucks[idx] <= L:
            bridge.append(trucks[idx])
            idx += 1
        else:
            bridge.append(0)
    else:
        if sum(bridge) == 0:
            break
print(time)

