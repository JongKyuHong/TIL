import sys
input = sys.stdin.readline

n, l = map(int, input().split())
road = [0]*l
time = 0
for i in range(n):
    d, r, g = map(int, input().split()) # 신호등 위치, 빨간색 초록색 지속되는 시간
    color = r+g
    if i == 0:
        time = d
    else:
        time += (d-prev)
    target = time % color
    if target <= r:
        time += abs(target-r)
    prev = d
#print(d)
print(time+l-d)

    
