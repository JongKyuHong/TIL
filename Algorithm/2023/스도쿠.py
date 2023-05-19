import sys
input = sys.stdin.readline

def check(r, c, nums, lst):
    nums = str(nums)
    for i in range(9):
        if nums == lst[r][i]:
            return 0
    for i in range(9):
        if nums == lst[i][c]:
            return 0
    if 0 <= r < 3:
        if 0 <= c < 3:
            for i in range(3):
                for j in range(3):
                    if nums == lst[i][j]:
                        return 0
        elif 3 <= c < 6:
            for i in range(3):
                for j in range(3, 6):
                    if nums == lst[i][j]:
                        return 0
        else:
            for i in range(3):
                for j in range(6, 9):
                    if nums == lst[i][j]:
                        return 0
    elif 3 <= r < 6:
        if 0 <= c < 3:
            for i in range(3, 6):
                for j in range(3):
                    if nums == lst[i][j]:
                        return 0
        elif 3 <= c < 6:
            for i in range(3, 6):
                for j in range(3, 6):
                    if nums == lst[i][j]:
                        return 0
        else:
            for i in range(3, 6):
                for j in range(6, 9):
                    if nums == lst[i][j]:
                        return 0
    else:
        if 0 <= c < 3:
            for i in range(6, 9):
                for j in range(3):
                    if nums == lst[i][j]:
                        return 0
        elif 3 <= c < 6:
            for i in range(6, 9):
                for j in range(3, 6):
                    if nums == lst[i][j]:
                        return 0
        else:
            for i in range(6, 9):
                for j in range(6, 9):
                    if nums == lst[i][j]:
                        return 0
    return 1

# def find(lst2):
#     while not done(lst2):
#         for i in range(9):
#             for j in range(9):
#                 if lst2[i][j] == '0':
#                     dfs(i, j, lst2)
#     return lst2

def dfs(r, c, lst2):
    if c == 9:
        r += 1
        c = 0
    if r == 9:
        for i in lst2:
            for j in i:
                print(j, end='')
            print()
        exit()
    if lst[r][c] == '0':
        nums = 1
        while nums < 10:
            if check(r, c, nums, lst2):
                lst2[r][c] = str(nums)
                dfs(r, c+1, lst2[:])
                lst2[r][c] = '0'
            nums += 1
    else:
        dfs(r, c+1, lst2)

def done(lst):
    for i in range(9):
        for j in range(9):
            if lst[i][j] == '0':
                return 0
    return 1

lst = [list(input().rstrip()) for _ in range(9)]
print(dfs(0, 0, lst[:]))
