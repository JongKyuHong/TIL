from re import A
import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

summary = 0
standard = sys.maxsize
S.sort() # 정렬
start = 0
end = N-1
min_v = []
while start < end:
    s_left = S[start] # 앞 뒤로 확인
    s_right = S[end]
    answer = s_left + s_right

    if abs(answer) < standard:
        standard = abs(answer)
        min_v = [start, end]
    
    if answer < 0: # 값이 0보다 작으면 늘려줘야하기때문에 왼쪽을 당김
        s_left += 1
    else: # 값이 0보다크면 오른쪽에서 당김
        s_right -= 1

print(min_v[0], min_v[1])
