from collections import defaultdict
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
share_card = list(map(int, input().split()))
team_card = list(map(int, input().split()))

# 1. 최적의 숫자 제거 <- 이게 키포인트
# 1-1. 어떻게 할것인가, 모두 다 곱해서 가장 큰 쌍을 K개 제거한 후 그 다음 큰것
# 1-2. 딕셔너리 통해서 어떤 인덱스에서 최대값이 나왔는지?

ans = defaultdict(int)
for i in range(N):
    for j in range(N):
        if ans[i]:
            ans[i] = max(ans[i], team_card[i]*share_card[j])
        else:
            ans[i] = team_card[i]*share_card[j]

ans = sorted(ans.items(), key=lambda x: x[1])
print(ans[-(K+1)][1])