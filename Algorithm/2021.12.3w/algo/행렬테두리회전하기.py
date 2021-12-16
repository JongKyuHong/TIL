import pprint

def solution(rows, columns, queries):
    answer = []
    graph = [[0]*columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = cnt
            cnt += 1
    for x1,y1,x2,y2 in queries:
        tmp = graph[x1-1][y1-1]
        mini = tmp
        
        for k in range(x1-1,x2-1):
            test = graph[k+1][y1-1]
            graph[k][y1-1] = test
            mini = min(mini, test)
            pprint.pprint(graph)
            
        for k in range(y1-1,y2-1): # 하단 가로
            test = graph[x2-1][k+1]
            graph[x2-1][k] = test
            mini = min(mini, test)
            pprint.pprint(graph)

        for k in range(x2-1,x1-1,-1): # 왼쪽 세로
            test = graph[k-1][y2-1]
            graph[k][y2-1] = test
            mini = min(mini, test)
            pprint.pprint(graph)

        for k in range(y2-1,y1-1,-1): # 상단 가로
            test = graph[x1-1][k-1]
            graph[x1-1][k] = test
            mini = min(mini, test)
            pprint.pprint(graph)
        
        graph[x1-1][y1] = tmp
        answer.append(mini)
    
    return answer

pprint.pprint(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))