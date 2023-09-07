import heapq
import sys 
input = sys.stdin.readline

N = int(input())
q = []
lst = []
for _ in range(N):
    number, start, end = map(int, input().split())
    lst.append((start, end, number))
lst.sort(key=lambda x:x[0])

for start, end, number in lst:
    if q: # 가장 end시간이 임박한 친구를 데려옴? q안에 다른 애들까지 확인하고 연달아서 강의 들을 수있는 친구는 연장해버림
        flag = 0
        for i in range(len(q)):
            if q[i] <= start:
                q[i] = end
                flag = 1
                break
        if not flag:
            heapq.heappush(q, end)
    else:
        heapq.heappush(q, end)
print(len(q))