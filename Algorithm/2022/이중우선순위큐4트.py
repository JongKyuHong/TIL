import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    max_heap = []
    min_heap = []
    visited = []
    idx = 0
    for _ in range(int(input())):
        k, n = input().rstrip().split()
        n = int(n)
        if k == 'I':
           heapq.heappush(max_heap, [-n, idx])
           heapq.heappush(min_heap, [n, idx])
           visited.append(1)
           idx += 1
        else:
            if max_heap and min_heap:
                if n == -1:
                    # 최솟값 삭제 원래 힙 기능쓰기
                    while min_heap and not visited[min_heap[0][1]]:
                        min_v, min_idx = heapq.heappop(min_heap) # 최소 힙이 있을때 pop을 한다.
                    
                    if min_heap:
                        min_v, min_idx = heapq.heappop(min_heap)
                        visited[min_idx] = 0
                    
                else:
                    # 최댓값 삭제
                    while max_heap and not visited[max_heap[0][1]]:
                        heapq.heappop(max_heap)
                        
                            
                    if max_heap:
                        max_v, max_idx = heapq.heappop(max_heap)
                        visited[max_idx] = 0

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')