import heapq

n = int(input())
timetable = [list(map(int,input().split())) for _ in range(n)]
que = []
heapq.heappush(que, timetable[0][1])

for i in range(1,n):
    if que[0] > timetable[i][1]:
        heapq.heappush(que, timetable[i][1])
    else:
        heapq.heappop(que)
        heapq.heappush(que, timetable[i][1])

print(len(que))