import sys 
input = sys.stdin.readline

n, m = map(int, input().split())

road = []
prev = 0
for _ in range(n):
    length, speed = map(int, input().split())
    road.append([prev, length+prev, speed])
    prev += length
yeon = []
prev = 0
for _ in range(m):
    length, speed = map(int, input().split())
    yeon.append([prev, length, speed])
    prev += length
max_speed = 0
y_idx = 0
r_idx = 0

while r_idx < len(road):
    start, end, speed = yeon[y_idx]
    road_start, road_end, limit_speed = road[r_idx]
    if road_start <= start or road_start <= end:
        if road_end < end:
            max_speed = max(max_speed, speed-limit_speed)

print(max_speed)