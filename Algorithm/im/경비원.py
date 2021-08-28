def dist_calc(idx, pos):  # 일단 시계방향으로
    if idx == 1:  # 북쪽
        return pos
    elif idx == 2:  # 남쪽
        return c + r + c - pos  
    elif idx == 3:  # 서쪽
        return c + r + c + r - pos
    else:  # 동쪽
        return c + pos


c,r = map(int, input().split())
circumference = (c+r)*2 # 둘레
n = int(input())

dist = []
for i in range(n+1):
    idx, pos = map(int, input().split())  # 어떤 면인지와, 위치
    dist.append(dist_calc(idx, pos))
my_dist = dist[-1]

ans = 0

for i in range(n):
    clockwise = abs(my_dist-dist[i])
    ans += min(clockwise,circumference- clockwise)  # 반대방향중 어느게 더 작은지
print(ans)
    



