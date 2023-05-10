from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
lst = deque(list(map(int, input().split())))
lst = deque(enumerate(lst))
dir = 0 # 0은 정방향 1은 역방향으로 생각
ans = [1]
rotate_cnt = lst.popleft()[1]
idx = 1
while len(ans) < N:
    if rotate_cnt > 0:
        while rotate_cnt > 0:
            rotate_cnt -= 1
            tmp_idx, tmp_value = lst.popleft()
            if rotate_cnt == 0:
                rotate_cnt = tmp_value
                ans.append(tmp_idx+1)
                break
            else:
                idx += 1
                lst.append((tmp_idx, tmp_value))    
    else:
        while rotate_cnt < 0:
            rotate_cnt += 1
            tmp_idx, tmp_value = lst.pop()
            if rotate_cnt == 0:
                rotate_cnt = tmp_value
                ans.append(tmp_idx+1)
                break
            else:
                idx -= 1
                lst.appendleft((tmp_idx, tmp_value))
print(*ans)
    


