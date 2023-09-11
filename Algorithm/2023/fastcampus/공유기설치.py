from itertools import combinations
import sys 
input = sys.stdin.readline

N, C = map(int, input().split())
lst = []
for _ in range(N):
    inp = int(input())
    lst.append(inp)

# 음..
# 탐색을 어떻게 해야할지
# 크게 생각나는 알고리즘은 완전탐색, 이분탐색 등이 있다. 
# 내가 생각할때 이분탐색 문제는 아닌거같음
# 아래 실수로 내려보니까 이분탐색문제였음 ㅋㅋ;
# 어느 경우에 이분탐색을 사용해야하는지 잘모르겠다
# 일단 이분탐색이니까 정렬되어있는 데이터를 기준으로 탐색하기때문에 리스트를 정렬한다
lst.sort()

# 배치를 어떻게 하는지에 따라 최대 
# for com in combinations(lst, C):
# combination으로 모든 경우를 다보려고 했는데 이건 의미가 없는거같고
def solve(value):
    remain_cnt = C-1
    tmp = lst[0]
    for i in range(1, N):
        if lst[i] - tmp >= value:
            tmp = lst[i]
            remain_cnt -= 1
    if remain_cnt <= 0:
        return 1
    else:
        return 0

# 최대 거리를 이분탐색으로 하는게 나은것같다.
# combi로 모든경우를 보면서 각각의 경우에서 가장작은값이 가장 큰경우를 찾는다 근데 이게그냥 답아닌가 그러면



start, end = 0, lst[N-1] - lst[0]
answer = 0
while start <= end:
    mid = (start+end)//2
    # 최대가 mid일때 
    if solve(mid):
        answer = max(answer, mid) # mid가 더 큰경우도 있는지 봐야하므로
        start = mid + 1
    else:
        end = mid - 1
print(answer)

