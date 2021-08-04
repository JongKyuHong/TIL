# from collections import deque

# n,k = map(int,input().split())
# array = list(map(int,input().split()))

# # 전략 
# # 1. 실제 멀티탭 리스트를 만들어서 그 안에 데이터를 넣고 (실제 멀티탭에 꽂혀있는것처럼 생각)
# # 2. 멀티탭 길이만큼 검사를한다 array를
# # 3. 만약에 멀티탭에 꽂혀있지 않은 값이 나오면 뒤에도 없는 값을 뺀다. 예시 234가 꽂혀있는데 435가 들어오면 자연스레 
# # 4. 2가 빠진다.
# multitap = []
# que = deque(array)
# for i in range(n):
#     multitap.append(que.popleft())

# while que:
#     q = que.popleft()
#     if multitap not in q:
#         for i in range(n-1):
#             q1 = que.popleft()
#             if q1 in multitap:
#                 multitap

from sys import stdin
N, K = stdin.readline().split()
N = int(N)
K = int(K)
multap = [0] * N
li = list(map(int, stdin.readline().split()))
res = swap = num = max_I = 0
for i in li:
    if i in multap:
        pass
    elif 0 in multap:
        multap[multap.index(0)] = i
    else:
        for j in multap:
            if j not in li[num:]:
                swap = j
                break
            elif li[num:].index(j) > max_I:
                max_I = li[num:].index(j)
                swap = j
        multap[multap.index(swap)] = i
        max_I = swap = 0
        res += 1
    num += 1
print(res)

## 너무 좋은 코드 (물론 인터넷에서 가져온) 멀티탭 리스트에 직접 값을넣어서 비교하기가 굉장히 편했다.
## 0인경우 빈것으로 판단해서 새로운 값을 넣어주고
## num을통해 뒤에 값이 언제나오는지 확인한다.
## 그리드문제는 항상 for문을 쓸지 whiile문을 쓸지가 제일 어렵고 특히 반복문 조건을 정하는것이 가장 힘든것같다.
