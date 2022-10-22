from collections import deque

def solution(begin, target, words):
    INF = float('inf')
    answer = INF
    q = deque()
    visited = [0]*len(words)
    q.append((begin, 0))
    while q:
        begin, cnt = q.popleft()
        if begin == target:
            answer = min(answer, cnt)
            continue
        for word in range(len(words)):
            if not visited[word]:
                tmp = 0
                for i in range(len(words[word])):
                    if begin[i] != words[word][i]:
                        tmp += 1
                if tmp == 1:
                    visited[word] = 1
                    q.append((words[word],cnt+1))
    return answer if answer != INF else 0
        
                
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))