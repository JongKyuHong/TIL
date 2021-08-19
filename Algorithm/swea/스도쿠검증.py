t = int(input())


def check_row(arr):
    for i in range(9):
        result = [0]*10
        for j in range(9):
            if result[arr[i][j]] == -1:
                return False
            result[arr[i][j]] -= 1
    return True

def check_col(arr):
    for i in range(9):
        result = [0]*10
        for j in range(9):
            if result[arr[j][i]] == -1:
                return False
            result[arr[j][i]] -= 1
    return True


def check_3x3(arr):
    for i in range(0,7,3):
        for j in range(0,7,3):
            result = [0]*10
            for x in range(3):
                for y in range(3):
                    if result[arr[i+x][j+y]] == -1:
                        return False
                    result[arr[i+x][j+y]] -= 1
                    
    return True
    
for test_case in range(1,t+1):
    matrix = [list(map(int,input().split())) for _ in range(9)]
    if not check_row(matrix):
        print(f'#{test_case} 0')
    elif not check_col(matrix):
        print(f'#{test_case} 0')
    elif not check_3x3(matrix):
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')



