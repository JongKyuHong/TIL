import heapq
import sys
input = sys.stdin.readline

def find(time, v):
    q = [(time, v)]
    dist[v] = 0 # 시작지점의 시간을 초기화
    while q:
        time, v = heapq.heappop(q)
        if dist[v] < time:
            continue
        for i in range(3):
            if i == 0:
                num = v+1
                if 0 <= num <= 100001 and dist[num] > time+1:
                    dist[num] = time+1
                    heapq.heappush(q, (time+1, num))
            elif i == 1:
                num = v-1
                if 0 <= num <= 100001 and dist[num] > time+1:
                    dist[num] = time+1
                    heapq.heappush(q, (time+1, num))
            else:
                num = v*2
                if 0 <= num <= 100001 and dist[num] > time:
                    dist[num] = time
                    heapq.heappush(q, (time, num))

n, k = map(int, input().split()) # 수빈이가 있는 위치, 동생이 있는 위치
dist = [sys.maxsize] * 100002
find(0, n) # 이동시간, 시작지점
print(dist[k])
