from collections import deque
import sys
input = sys.stdin.readline

N, B, W = map(int, input().split()) # 조약돌갯수, 검은 조약돌, 하얀 조약돌
inp = input().rstrip()

string = deque([])
max_v = 0
black, white = 0, 0
end = 0

for start in range(N):
    while end < N and black <= B:
        if inp[end] == 'B':
            black += 1
            if black > B:
                black -= 1
                break
        elif inp[end] == 'W':
            white += 1
        string.append(inp[end])
        end += 1
        #print(end,'end')
    #print(end,'end2')
    if white >= W and black <= B:
        max_v = max(max_v, len(string))
    if string:
        target = string.popleft()
        if target == 'B':
            black -= 1
        elif target == 'W':
            white -= 1
    else:
        end += 1
print(max_v)

