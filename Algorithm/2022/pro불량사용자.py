def solution(user_id, banned_id):
    answer = 0
    visited = []
    def dfs(idx, jdx):
        nonlocal user_id, banned_id, answer
        if jdx == len(banned_id):
            if sorted(idx) not in visited:
                visited.append(sorted(idx))
                answer += 1
            return
        
        for i in range(len(user_id)):
            if i not in idx:
                if len(user_id[i]) == len(banned_id[jdx]):
                    flag = 0
                    for a, b in zip(user_id[i],banned_id[jdx]):
                        if a == b or b == '*':
                            continue
                        else:
                            flag = 1
                            break
                    if not flag:
                        dfs(idx+[i], jdx+1)

    for i in range(len(user_id)):
        if len(user_id[i]) == len(banned_id[0]):
            flag = 0
            for a, b in zip(user_id[i],banned_id[0]):
                if a == b or b == '*':
                    continue
                else:
                    flag = 1
                    break
            if not flag:
                dfs([i], 1)
                        
    return answer