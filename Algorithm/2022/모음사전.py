def solution(word):
    answer = 0
    w = ['A','E','I','O','U']
    def dfs(depth, tmp):
        if depth == 5:
            return
        for i in range(5):
            if not visited[depth][i]:
                visited[depth][i] = 1
                res.append(tmp+w[i])
                dfs(depth+1, tmp+w[i])
                visited[depth][i] = 0
    
    visited = [[0]*5 for _ in range(5)]
    res = []
    for i in range(5):
        visited[0][i] = 1
        res.append(w[i])
        dfs(1, w[i])
        visited[0][i] = 0
    res.sort()
    return res.index(word)+1

print(solution('AAAAE'))
print(solution('AAAE'))
print(solution('I'))