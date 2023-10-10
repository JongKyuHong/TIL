from collections import deque
import sys 
input = sys.stdin.readline

def solve(arr, xcnt, ocnt):
    # 4.
    xtmp = 0
    otmp = 0
    if lst[0][0] == lst[0][1] == lst[0][2]:
        if lst[0][0] == 'X':
            xtmp += 1
        elif lst[0][0] == 'O':
            otmp += 1

    if lst[1][0] == lst[1][1] == lst[1][2]:
        if lst[1][0] == 'X':
            xtmp += 1
        elif lst[1][0] == 'O':
            otmp += 1

    if lst[2][0] == lst[2][1] == lst[2][2]:
        if lst[2][0] == 'X':
            xtmp += 1
        elif lst[2][0] == 'O':
            otmp += 1
    
    if lst[0][0] == lst[1][0] == lst[2][0]:
        if lst[0][0] == 'X':
            xtmp += 1
        elif lst[0][0] == 'O':
            otmp += 1

    if lst[0][1] == lst[1][1] == lst[2][1]:
        if lst[0][1] == 'X':
            xtmp += 1
        elif lst[0][1] == 'O':
            otmp += 1

    if lst[0][2] == lst[1][2] == lst[2][2]:
        if lst[0][2] == 'X':
            xtmp += 1
        elif lst[0][2] == 'O':
            otmp += 1        

    if lst[0][0] == lst[1][1] == lst[2][2]:
        if lst[0][0] == 'X':
            xtmp += 1
        elif lst[0][0] == 'O':
            otmp += 1
    
    if lst[0][2] == lst[1][1] == lst[2][0]:
        if lst[0][2] == 'X':
            xtmp += 1
        elif lst[0][2] == 'O':
            otmp += 1

    if xtmp == 0 and otmp == 0: # 미완성
        if xcnt + ocnt == 9:
            return 1
        else:
            return 0
    elif xtmp == 1:
        if otmp == 1 or xcnt <= ocnt:
            return 0
        else:
            return 1
    elif otmp == 1: # o가 이겼을때
        if xcnt > ocnt:
            return 0
        else:
            return 1
    elif xtmp > 1:
        if xcnt ==  ocnt + 1:
            return 1
        else:
            return 0
    elif otmp > 1:
        return 0

    # 0. X의 갯수가 더 적은 경우는 함수 들어오기전에 제하였다.
    # 1. 무조건 첫번째 사람이 X를 놓음
    # 2. 가로, 세로, 대각선 방향으로 3칸을 잇는데 성공하면 끝남
        # 2-1. 내 주변에 나랑 다른 블럭이 있으면 무조건 성립하는가?
        # 2-1. 안됨, XOXXXXOOO 숨구멍이 안트여있는 경우가 있다. 
        
        # 2-2. 모든 X에 대해서 게임을 시작하면 어떻게 될까? bfs로 탐색한다.
        # 2-2. 내가 X인경우 O을 찾음, 찾으면 q에넣음, visited는 1, O인경우 반대로 진행, 모두 끝났을때 .이 있는
        # 인덱스를 제외한 모든 구역을 탐색할 수 있는가?를 반복
        # 2-2. 이렇게 생각하는 근거
        # X가 5인경우(최대치) 5번 탐색을 하는데 탐색범위가 작아서 생각보다 시간이 덜걸림
        # 입력의 갯수가 얼마나 되는지는 모르겠으나 그렇게 시간적으로 무리가 갈 것 같지않음

    # 3. 게임판이 가득차도 끝난다. (유효하다면?)

    # 4. X가 이어져 있는 경우
    # 4-1. 안되는 경우는 O도 이어져 있는 경우 하나이다.


while 1:
    inp = input().rstrip()
    if inp == 'end':
        break
    lst = []
    idx = 0
    if inp.count('X') < inp.count('O'): # 같을수는 있다.
        print("invalid")
        continue
    elif inp.count('X') > inp.count('O') + 1:
        print("invalid")
        continue
    
    for i in range(3):
        lst.append(inp[idx:idx+3])
        idx += 3

    if solve(lst, inp.count('X'), inp.count('O')):
        print('valid')
    else:
        print('invalid')