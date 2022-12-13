def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    
    def check(r, c):
        gap = 1
        while r+gap < n and c+gap < m:
            for i in range(c, c+gap):
                if not board[r+gap][i]:
                    return gap-1
            for i in range(r, r+gap):
                if not board[i][c+gap]:
                    return gap-1
            gap += 1
        return gap
        
    idx = 0
    jdx = 0
    while idx < n:
        if board[idx][jdx]:
            value = check(idx, jdx)
            if answer < value:
                idx += value
                jdx = 0
                answer = value
            else:
                jdx += 1
                if jdx == m:
                    idx += 1
                    jdx = 0
        else:
            jdx += 1
            if jdx == m:
                idx += 1
                jdx = 0
        print(idx, jdx)
    return answer**2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))