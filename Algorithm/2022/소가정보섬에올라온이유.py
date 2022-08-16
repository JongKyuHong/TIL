import sys
input = sys.stdin.readline

n, q = map(int, input().rstrip().split()) # 소의수, 욱제가 장난칠 횟수
cows = list(map(int, input().rstrip().split())) # 소들의 품질점수
joke = list(map(int, input().rstrip().split())) # 장난 칠 Q개의 소의 번호

# 연속한 네마리 소들의 품질 점수를 곱한 값을 모두 (정확히 한 번씩)더한 것이다.
# 장난은 -1을 곱하면된다.

nums = [0]*n

for i in range(n):
    nums[i] = cows[i]*cows[i-1]*cows[i-2]*cows[i-3]

ex_sum = sum(nums)
for i in joke:
    for j in range(4):
        idx = (i+j-1)%n
        nums[idx] = -nums[idx]
        print(nums[idx],'num idx')
        ex_sum += 2*nums[idx]
    print(ex_sum)