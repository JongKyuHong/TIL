import sys
sys.stdin = open('input.txt')


def check_row(arr):
    maxa = 0
    for i in arr:
        maxa = max(maxa,sum(i))
    return maxa


def check_col(arr):
    maxa = 0

    for i in range(100):
        cnt = 0
        for j in range(100):
            cnt += arr[j][i]
        maxa = max(maxa,cnt)
    return maxa


def check_x(arr):
    maxa = 0
    cnt = 0
    for i in range(100):
        cnt += arr[i][i]
    cnt2 = 0
    for i in range(100):
        cnt2 += arr[i][99-i]
    if cnt > cnt2:
        maxa = cnt
    else:
        maxa = cnt2
    return maxa

for _ in range(10):
    tc = int(input())
    matrix = [list(map(int,input().split())) for _ in range(100)]
    row_max = check_row(matrix)
    col_max = check_col(matrix)
    x_max = check_x(matrix)
    res = max(row_max,col_max,x_max)
    print(f'#{tc} {res}')
    



