# 2021/12/12

------------------

경로찾기

* 전체 그래프의 간선연결정보를 알아야 하기때문에 플로이드워셜알고리즘으로 해결

* 플로이드워셜이 잘 기억나지않아서 하루일과의 플로이드워셜을 참고

* 3중for문 사용

  ```
  graph[a][k] + graph[k][a]사용
  ```



숫자문자열과 영단어

* 문자열 조작
* 문자열이 숫자의 의미를 가지면 answer에 바로 넣고 문자열의 의미를 가지면 res변수에 따로 저장하고 res변수값이 딕셔너리 키값에 존재한다면 answer에 넣어주고 res초기화
* 딕셔너리를 오랜만에 다루어서 버벅거렸다.., keys를 이용해서 계속 비교하는것을 생각하지 못하여서 웹서핑을 통해서 해결



3진법 뒤집기

* https://programmers.co.kr/learn/courses/30/lessons/68935
* int(n,3)을 통하여 변환이 되는줄 알았으나 3이상의 수가 포함되면 오류가 난다는것을 깨달았다.
* divmod를 통해 몫과 나머지로 분류하고 answer에 더해가는 식으로 구하였다.
* 참고 https://velog.io/@qmasem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-3%EC%A7%84%EB%B2%95-%EB%92%A4%EC%A7%91%EA%B8%B0-Python

* 생각보다 level1에서 배우는게 많은것같다.



2021/12/13

----------------------------

문자열 압축 

* https://programmers.co.kr/learn/courses/30/lessons/60057
* 문자열을 압축하는 과정에서 버벅거렸고, 문자열 슬라이싱을 통해서 극복하였다.
* for문을 두개를 돌려서 구현하면되는 간단한 문제인데 집중을 제대로 못했던것같다.



2021/12/15

-----------------------

내리막 길

* https://www.acmicpc.net/problem/1520

* dfs문제

* ```python
  def dfs(r, c, visited):
      for dr, dc in delta:
          nr = dr + r
          nc = dc + c
          if nr == (m-1) and nc == (n-1):
              global count
              count += 1
              continue
          if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and graph[nr][nc] < graph[r][c]:    
              visited[nr][nc] = 1
              dfs(nr, nc, visited)
              visited[nr][nc] = 0
  
  delta = ((0,1),(0,-1),(1,0))
  m, n = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range(m)]
  visited = [[0]*n for _ in range(m)]
  count = 0
  visited[0][0] = 1
  dfs(0,0, visited)
  print(count)
  ```

  초기코드를 이렇게 구성하니까 시간초과가 났다.

* ```python
  def dfs(r, c):
      if r == 0 and c == 0:  # 초기값이 0,0 이면 1리턴하고 끝
          return 1
      if visited[r][c] == -1:  # 처음 접근하는 곳이면 1증가, 이미 접근한 곳이면 visited값 리턴
          visited[r][c] += 1
          for dr, dc in delta:
              nr = dr + r
              nc = dc + c
              if 0 <= nr < m and 0 <= nc < n:
                  if graph[r][c] < graph[nr][nc]:  # 조건에 부합하면
                      visited[r][c] += dfs(nr, nc)  # dfs리턴값을 visited에 더해준다.
      return visited[r][c] 
                  
  delta = ((0,1),(0,-1),(1,0),(-1,0))
  m, n = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range(m)]
  visited = [[-1]*n for _ in range(m)]
  visited[0][0] = 1
  result = dfs(m-1,n-1)
  print(result)
  ```

  역으로 m-1 n-1부터 시작을해서 접근
