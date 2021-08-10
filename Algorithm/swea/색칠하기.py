t = int(input())

for test_case in range(1,t+1):
    n = int(input())  # 칠할 영역
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))  # 모서리 인덱스, 색깔 등록
    graph = [['0']*10 for i in range(10)]  # 2차원리스트 생성
    while array:
        r1,c1,r2,c2,color=array.pop(0)
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                if color == 1:
                    graph[i][j] += '1'  # color가 1이면 1추가
                else:
                    graph[i][j] += '2'  # color가 2이면 2추가
    cnt = 0
    for i in graph:
        for j in i:
            if '1' in j and '2' in j:  # 1과 2가 모두 들어있으면 
                cnt += 1  # 갯수 1증가
    print(f'#{test_case} {cnt}')



     