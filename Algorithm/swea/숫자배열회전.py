t = int(input())

def rotate(arr):
    n = len(arr)
    m = len(arr[0])

    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = arr[i][j]
    return result

for test_case in range(1,t+1):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    rotate_90 = rotate(matrix)
    rotate_180 = rotate(rotate_90)
    rotate_270 = rotate(rotate_180)
    print(f'#{test_case}')
    for i in range(n):
        print(*rotate_90[i], *rotate_180[i], *rotate_270[i])
    
    



