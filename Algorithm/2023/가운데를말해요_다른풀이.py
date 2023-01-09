import sys
import heapq
input = sys.stdin.readline

N = int(input())

left, right = [], []
answer = []
for i in range(N):
    inp = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -inp)
    else:
        heapq.heappush(right, inp)
    if right and right[0] < -left[0]:
        lv = heapq.heappop(left)
        rv = heapq.heappop(right)
        heapq.heappush(left, -rv)
        heapq.heappush(right, -lv)
    
    print(-left[0])

# left의 첫원소를 중간값으로 생각하고 푸는 풀이
# right에 원소를 일단 넣고 left와 계속해서 비교