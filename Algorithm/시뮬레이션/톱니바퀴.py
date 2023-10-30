from collections import deque
import sys 
input = sys.stdin.readline

def rotate(idx, dir, tmp):
    if tmp == 1:
        if idx + 1 < 4:
            if lst[idx][2] != lst[idx+1][6]:
                if delta[idx+1] == -2:
                    delta[idx+1] = -1*dir
                    rotate(idx+1, -1*dir, tmp)
    elif tmp == -1:
        if idx - 1 >= 0:
            if lst[idx-1][2] != lst[idx][6]:
                if delta[idx-1] == -2:
                    delta[idx-1] = -1*dir
                    rotate(idx-1, -1*dir, tmp)

lst = [deque(list(input().rstrip())) for _ in range(4)]
K = int(input())

for _ in range(K):
    num, dir = map(int, input().split())
    delta = [-2, -2, -2, -2]
    delta[num-1] = dir
    rotate(num-1, dir, -1) # 왼쪽
    rotate(num-1, dir, 1) # 오른쪽
    for i in range(4):
        if delta[i] == -1:
            lst[i].rotate(-1)
        elif delta[i] == 1:
            lst[i].rotate(1)

answer = 0
if lst[0][0] ==  '1':
    answer += 1
if lst[1][0] == '1':
    answer += 2
if lst[2][0] == '1':
    answer += 4
if lst[3][0] == '1':
    answer += 8
print(answer)