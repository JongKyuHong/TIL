import sys
input = sys.stdin.readline

N, L = map(int, input().split()) # 
lst = sorted(list(map(int, input().split())))
start = 0
cnt = 0
for l in lst:
    if start < l:
        start = l+L-1
        cnt += 1
print(cnt)

# 1차 시도
# 1. 리스트 정렬
# 2. 앞에서부터 테이프를 붙임 좌우 0.5씩 여유공간이 있어야 하기 때문에 다음거와의 차이 +0.5보다 테이프의 길이가 크면
# 테이프에 포함되어있는 구멍이라고 볼 수 있다. (좌쪽으로도 0.5 간격차이가 있어야 하기때문에 +1로 생각하면 될듯)
# 3. 테이프는 겹쳐서 붙일수 있다.

# 2차 시도
# 1. 첫번째 인덱스값 - 0.5 부터 +L까지
