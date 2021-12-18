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

  이미 접근한곳은 visited값 리턴해서 해결하였다.

2021/12/16

---------------------

오픈채팅방

* https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
* 닉네임 변경을 어떻게 고려할지 아이디어를 못떠올렸는데 딕셔너리를 생성해서 아이디별로 닉네임을 미리 갱신해놓고 출력시에 들어왔다 나갔다만 표시하였다.



124나라의 숫자

* https://programmers.co.kr/learn/courses/30/lessons/12899
* 숫자가 1,2,4만 사용되는 문제이다.
* nums리스트를 만들고 [1,2,4] , n이 1일때 1이나와야하므로 인덱스를 -1해줘야 한다까지는 생각함
* answer에 nums[n%3]한 값을 계속 앞에다가 붙여주면서 계산하는것은 생각하지 못하였다..



짝지어 제거하기

* https://programmers.co.kr/learn/courses/30/lessons/12973

* 이런류의 문제는 스택으로 풀면 좋다는것을 기억해야할것 같다.

  

메뉴 리뉴얼

* https://programmers.co.kr/learn/courses/30/lessons/72411
* itertools의 combinations과 collections의 Counter를 사용하였다.
* combinations을 통하여 course의 값만큼 조합으로 뽑아내었고, Counter를 통하여 딕셔너리 형태로 카운팅을 한다.
* 딕셔너리 공부할때 좋은 문제이긴하나 import를 너무 많이 써서 import를 할수없는 환경에서는 풀기 어려울것으로 예상된다.



뉴스클러스터링

* https://programmers.co.kr/learn/courses/30/lessons/17677
* 바로 전 문제인 메뉴리뉴얼에서 사용했던 Counter를 사용하여 풀었다.



거리두기 확인하기

* https://programmers.co.kr/learn/courses/30/lessons/81302
* 일반 bfs문제에 얼마나 걸었는지 정보를 q에포함



수식 최대화

* https://programmers.co.kr/learn/courses/30/lessons/67257
* 스택문제
* 어려웠다 일단 문자열에서 연산자를 어떻게 걸러낼지가 첫번째 난관이였고 (isdigit으로 걸러냄) 어떻게 우리가 정한 순서에 맞게 계산할지도 모르겠었는데 permutations으로 생성한 수열을 리스트로 받아서 하나씩 돌려가며 함수의 인자로 넘겨주었다.



두수의 합

* https://www.acmicpc.net/problem/3273
* 투포인터 실전에서 처음써봄



n번째 큰 수

* https://www.acmicpc.net/problem/2075
* 이 문제를 풀면서 우선순위큐, heapify에 대해서 공부를 좀더 해야겠다고 생각했다.



2021/12/18

--------------------------

2진수 8진수

* https://www.acmicpc.net/problem/1373

* 10진수 -> 2, 8, 16진수 변환
  * bin, oct, hex
* 2, 8, 16 진수 -> 10진수 변환
  * int('문자열', (2,8,16 중 하나))



문자열 폭발

* https://www.acmicpc.net/problem/9935

* 처음에는 replace함수를 백만번 돌려서 해결하려하였으나 출력초과가 나와서 실패하였다.

* 스택으로 푸는문제라는 생각은 하였지만 계속해서 폭발문자열의 제일 앞글자와 지금 들어온 문자를 비교하는 작업을 하여서 해결을 못하고있었다.

* 구글링을 통하여 문자열이 들어왔을때 폭발문자열의 제일 뒷부분과 비교하면 된다는 것을 알게되고 뒤를 비교하고 만약에 같다면 폭발문자열의 길이 length_t를 이용하여 아래 처럼 비교하면 된다는것을 알게되고 그렇게 해결하였다.

* ```python
  if stack[-1] == target[-1] and ''.join(stack[-length_t:]) == target:
      del stack[-length_t:]
  ```

  여기서 del은 함수가 아니고 예약어라고 한다. (특정 기능을 수행하도록 미리 예약되어있는 단어 and,True,False등과 같음) del array[인덱스] 형태로 사용하면 된다고 한다.
