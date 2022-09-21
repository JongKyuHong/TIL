def solution(land):
    def find(depth, res, col):
        nonlocal answer, len_land
        if depth == len_land:
            answer = max(answer, res)
            return
        for i in range(4):
            if col != i:
                find(depth+1, res+land[depth][i], i)
    answer = 0
    len_land = len(land)
    for i in range(4):
        find(1, land[0][i], i)

    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))