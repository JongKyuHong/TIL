def solution(rows, columns, queries):
    answer = []
    graph = [[0]*columns for _ in range(rows)]
    val = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = val
            val += 1
    
    for query in queries:
        sr,sc,er,ec = query
        sr-=1;sc-=1;er-=1;ec-=1
        val = rows*columns
        tmp1 = graph[sr][ec]
        for i in range(ec, sc-1, -1):
            graph[sr][i] = graph[sr][i-1]
            if i != sc:
                val = min(val, graph[sr][i])
            
        tmp2 = graph[er][ec]
        for i in range(er, sr, -1):
            if i == sr+1:
                graph[i][ec] = tmp1
            else:
                graph[i][ec] = graph[i-1][ec]
            val = min(val, graph[i][ec])
        tmp3 = graph[er][sc]
        for i in range(sc, ec):
            if i == ec-1:
                graph[er][i] = tmp2
            else:
                graph[er][i] = graph[er][i+1]
            val = min(val, graph[er][i])
        for i in range(sr, er):
            if i == er-1:
                graph[i][sc] = tmp3
            else:
                graph[i][sc] = graph[i+1][sc]
            val = min(val, graph[i][sc])
        for g in graph:
            print(g)
        answer.append(val)
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))