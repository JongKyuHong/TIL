import sys
input = sys.stdin.readline

def recur(x1, x2, y1, y2):
    if x2 - x1 == 1 or y2-y1==1:
        ans[matrix[y1][x1]] += 1
        return
    target = matrix[y1][x1]
    flag = 0
    for j in range(y1, y2):
        for i in range(x1, x2):
            if target != matrix[j][i]:
                flag = 1
                break
        if flag:
            break
    
    if flag:
        recur(x1, x1+(x2-x1)//3, y1, y1+(y2-y1)//3)
        recur(x1+(x2-x1)//3, x1+2*(x2-x1)//3, y1, y1+(y2-y1)//3)
        recur(x1+2*(x2-x1)//3, x2, y1, y1+(y2-y1)//3)
        recur(x1, x1+(x2-x1)//3, y1+(y2-y1)//3, y1+2*(y2-y1)//3)
        recur(x1+(x2-x1)//3, x1+2*(x2-x1)//3, y1+(y2-y1)//3, y1+2*(y2-y1)//3)
        recur(x1+2*(x2-x1)//3, x2, y1+(y2-y1)//3, y1+2*(y2-y1)//3)
        recur(x1, x1+(x2-x1)//3, y1+2*(y2-y1)//3, y1+3*(y2-y1)//3)
        recur(x1+(x2-x1)//3, x1+2*(x2-x1)//3, y1+2*(y2-y1)//3, y1+3*(y2-y1)//3)
        recur(x1+2*(x2-x1)//3, x2, y1+2*(y2-y1)//3, y1+3*(y2-y1)//3)
    else:
        ans[target] += 1

N = int(input())
ans = {1:0, -1:0, 0:0}
matrix = [list(map(int, input().split())) for _ in range(N)]
recur(0, N, 0, N)
print(ans[-1])
print(ans[0])
print(ans[1])