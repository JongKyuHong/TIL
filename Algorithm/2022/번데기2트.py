import sys
input = sys.stdin.readline

A = int(input()) # 게임을 진행하는 사람
T = int(input()) # 구하고자 하는 번째
target = int(input()) # 0이면 뻔, 1이면 데기
arr = [0,1,0,1,0,0,1,1]
idx = 0
human_idx = 0
while 1:
    if idx == len(arr):
        idx = 0
        arr.insert(4,0)
        arr.insert(-1,1)
        #print(arr)
    if human_idx == A:
        human_idx = 0
    if arr[idx] == target:
        T -= 1
    if T == 0:
        print(human_idx)
        break
    idx += 1
    human_idx += 1
