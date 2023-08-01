def solution(board):
    ans = {'X':0, 'O':0}
    X_flag, O_flag = 0, 0
    # 가로 확인
    for i in range(3):
        X_count, O_count = 0, 0
        for j in range(3):
            if board[i][j] == 'X':
                X_count += 1
            elif board[i][j] == 'O':
                O_count += 1
        if X_count == 3:
            X_flag = 1
        if O_count == 3:
            O_flag = 1

        ans['X'] += X_count
        ans['O'] += O_count
    
    #print(ans, X_flag, O_flag)
    # 세로 확인
    for j in range(3):
        X_count, O_count = 0, 0
        for i in range(3):
            if board[i][j] == 'X':
                X_count += 1
            elif board[i][j] == 'O':
                O_count += 1
        if X_count == 3:
            X_flag = 1
        if O_count == 3:
            O_flag = 1
    
    #print(ans, X_flag, O_flag)

    # 대각선
    X_count, O_count = 0, 0
    for i in range(3):
        if board[i][i] == 'X':
            X_count += 1
        elif board[i][i] == 'O':
            O_count += 1
    if X_count == 3:
        X_flag = 1
    if O_count == 3:
        O_flag = 1

    X_count, O_count = 0, 0
    for i, j in [[0, 2], [1, 1], [2, 0]]:
        if board[i][j] == 'X':
            X_count += 1
        elif board[i][j] == 'O':
            O_count += 1
    
    if X_count == 3:
        X_flag = 1
    if O_count == 3:
        O_flag = 1
    if ans['X'] > ans['O']:
        return 0
    elif ans['O'] > ans['X'] + 1:
        return 0
    elif X_flag == 1 and O_flag == 1:
        return 0
    elif X_flag == 1 and ans['O'] != ans['X']:
        return 0
    elif O_flag == 1 and ans['O'] != ans['X'] + 1:
        return 0
    
    return 1

# 모두 . 인경우,

# 안되는 경우
# O갯수보다 X갯수가 많은 경우
# O이나 X가 완성되었는데도 진행된 경우, O이 완성 되었을때 -> X의 갯수가 같으면 안됨, X가 완성되었을때 -> O의 갯수가 X보다 크면 안됨
# 

print(solution(["OXX", "OOX", "OXO"]))

# OXX
# OOX
# OXO