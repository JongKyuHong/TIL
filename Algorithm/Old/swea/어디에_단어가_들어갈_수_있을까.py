t = int(input())

for test_case in range(1,t+1):
    n,k = map(int,input().split())  # 단어퍼즐의 가로세로길이, 단어의길이
    array = [list(map(int,input().split())) for _ in range(n)]
    total = 0
    cnt_list = [0 for _ in range(n+1)]  # k길이의 단어가 들어갈수 있는 자릿수 저장
    for i in range(n):
        cnt = 1  # 횟수
        prev = 2  # 아예 관련없는 값으로 저장
        for j in range(n):
            if prev == array[i][j]:  # prev값이 자기와 같을때
                cnt += 1  # 횟수 증가
            else:
                if prev == 1:  # prev값이 자기와 다르고 prev값이 1일때
                    prev = array[i][j]  # prev값을 현재값으로 바꾸고
                    cnt_list[cnt] += 1  # 횟수는 횟수리스트에 저장
                    cnt = 1  # 횟수 초기화
                else:
                    prev = array[i][j]  # 0일경우prev값과 cnt만 변경해줌
                    cnt = 1
            # 위에서는 prev값과 현재값이 바뀔때만 횟수 리스트에 저장했으므로
            # 행의 마지막 값 확인
            if j == n-1:  
                if prev == 1:
                    cnt_list[cnt] += 1
    for i in range(n):
        cnt = 1
        prev = 2
        for j in range(n):
            if prev == array[j][i]:
                cnt += 1
            else:
                if prev == 1:
                    prev = array[j][i]
                    cnt_list[cnt] += 1
                    cnt = 1
                else:
                    prev = array[j][i]
                    cnt = 1
            # 위에서는 prev값과 현재값이 바뀔때만 횟수 리스트에 저장했으므로
            # 열의 마지막 값 확인
            if j == n-1:
                if prev == 1:
                    cnt_list[cnt] += 1
    total = cnt_list[k]
    print(f'#{test_case} {total}')


