for test_case in range(10):
  N=int(input())      # 정점의 총 수
  result=1
  for n in range(N) :
    info=list(input().split())    # 정점 번호, 숫자 or 연산자, 왼쪽 자손, 오른쪽 자손
    if info[1].isdigit() == 0 :   # 연산자면 왼쪽 자손, 오른쪽 자손 다 있어야 함
      if len(info) < 4 :		# 입력 최대 길이 4가 되어야 함.
        result=0    # 유효성 검사 통과 실패
  
  print(f"#{test_case+1} {result}")