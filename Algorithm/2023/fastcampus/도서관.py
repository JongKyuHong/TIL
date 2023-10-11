import sys 
input = sys.stdin.readline

def solution(arr):
    global answer, flag
    tmp = 0
    cnt = 0
    flag2 = 0 # 첫 뭉텅이 나갈때
    while arr: # left라면
        if tmp == 0:
            tmp = arr.pop(0)
        else:
            arr.pop(0)
        cnt += 1
        if not arr: # 더이상 남은 lst가 없으면
            if flag == 0:
                answer += abs(tmp) * 2
            else: # flag가 있고
                if flag2 == 0: # 첫 뭉텅이에서 그냥 끝났으면
                    answer += abs(tmp)
                    return
                else:
                    answer += abs(tmp) * 2
            break
        if cnt == M:
            if flag == 1:
                if flag2 == 0:
                    answer += abs(tmp)
                    flag2 = 1
                else:
                    answer += abs(tmp)*2
            else:
                answer += abs(tmp) * 2
            tmp = 0
            cnt = 0
    flag += 1

        

N, M = map(int, input().split())
lst = list(map(int, input().split()))
left, right = [], []
left_maxv, right_maxv = 0, 0
for i in lst:
    if i > 0:
        right.append(i)
        right_maxv = max(right_maxv, i)
    else:
        left.append(i)
        left_maxv = max(left_maxv, abs(i))
answer = 0
flag = 0
if left_maxv > right_maxv:
    right.sort(reverse=True) # 
    left.sort()
    solution(right)
    solution(left)
    print(answer)
else: 
    left.sort()
    right.sort(reverse=True) 
    solution(left)
    solution(right)
    print(answer)