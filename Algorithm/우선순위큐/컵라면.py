

# 무조건 해당 시간에서 가장 큰것을 가져오는것이 아니다.
# 1 2 3  3
# 1 1 10 10

# 가장 많은 컵라면 수를 가져올수 있는게 문제
# 무조건 큰거먼저 <- 이것도 안됨

# 1  2  3  3
# 50 30 60 70
# 130, 180

# 우선순위 큐랑 뭔상관??
# 
# dp[타임][인덱스][0, 1] 인덱스 이번거 선택 or 안선택
# dp[1][1][0] --> 이번거 안선택 value = 0, idx만 증가
# dp[2][1][1] --> 이번거 선택 인덱스 증가 + 타임 증가
# 




#dp[1][0]  인덱스는 0부터 타임은 1부터 시작


# 이렇게 하면 안됨 무조건 첫번째것을 선택하는 것이니까
# deadline, cupramen_cnt = heapq.heappop(q)
# dp[2][0] = cupramen_cnt # 선택 한 경우
# dp[1][0] = 0

# 1. 실습 (망함)
# dp = [[0]*200001 for _ in range(200001)]

# time = 1
# idx = 0
# while q:
#     deadline, cupramen_cnt = heapq.heappop(q)
#     cupramen_cnt *= -1
#     # 두번
#     dp[time+1][idx] = max(dp[time+1][idx], dp[time][idx] + cupramen_cnt)


# 2. 0과 1로 선택한경우 안한경우를 나누면
# dp[idx][0] = 0
# dp[idx][1] = cupramen_cnt

# 타임은 어떻게 표시? --> 만약에 다 선택하는 경우에 타임 제약은 어떻게 걸것인가.cupramen_cnt


# 3. 삼차리스트로 표현한다면? 23:09 1번으로 채택
# dp[time][idx][0] = 0
# dp[time][idx][1] = cupramen_cnt 만약에 이렇게 표시했다면 선택한 경우에 time+1을 해주어야 할것이다. 즉 dp[time][idx][1] 과 dp[time+1][idx+1][0], dp[time+1][idx+1][1] 로 이어지게 되는데


# 1  2  3  3
# 50 30 60 70
# 180 

# 이라고 할때

# 0  --> 안선택 0 --> 안선택 0 --> 안선택 0
#                             --> 선택 70
#                 --> 선택 60 --> 안선택 0
#                             --> 선택 130
#    --> 선택 30, time = 2 --> 안선택
# 50

# 타임은 그냥 자유롭게 두고 타임이 데드라인의 최대값을 넘어간 경우 그냥 무시한다.

# 실습 ------------ (망함, dp 첫 조건을 어떻게 세워야 할지 모르겠음, 처음 초기값을 어떻게 지정해야 하는지)

# dp = [[[[0] * 2] for _ in range(N+1)] for _ in range(max_deadline)]

# idx = 0
# time = 1
# while q:
#     deadline, cupramen_cnt = heapq.heappop(q)
#     dp[time][idx][0] = # 선택 안하면 무슨값?
#     dp[time+1][idx][1] = # 선택함으로써 time은 올라갔음 무슨값 넣을거냐 뭐 + 뭐가 없다


# 4. 반대로 생각한다면?
# time이 max_deadline 부터 시작해서 아래로 내려옴 만약 time이 deadline보다 크면 더하기 안함, time이 deadline보다 작거나 같으면 더함

# 1  2  3  3 
# 50 30 60 70 
    
# 1 1 2 2 3 3 6
# 1 2 4 5 3 4 1

# 1. time = max_deadline
# 2. time은 계속해서 -1
# 3. time이 deadline보다 크면 무시 다시 q에 넣고 time -1
# 4. time이 deadline보다 작거나 같으면 계속 뽑음 가능한 애들을 게중에서 가장 큰값 선택 time -1 나머지 값들은 다시 q에넣음
# 5. 이렇게 time이 0 될때까지 반복

# 실습 (또망함 시간초과 내가볼때는 처음에는 그냥 리스트로 관리하다가 중간에 이제 가능한 값중 가장 큰값 고를때 우선순위큐를 도입해서 고르면 될것같음? 아니면 처음도 우선순위 중간도 우선순위 2배럭 메타로다가)

# time = max_deadline
# total_cupramen_cnt = 0
# while q and time > 0:
#     deadline, cupramen_cnt = heapq.heappop(q)
#     deadline *= -1; cupramen_cnt *= -1
#     #print(deadline, cupramen_cnt, time, total_cupramen_cnt, 'time')
#     if time <= deadline:
#         lst = [[deadline, cupramen_cnt]]
#         while q:
#             d, c = heapq.heappop(q)
#             d *= -1; c *= -1
#             if time <= d:
#                 lst.append([d, c])
#             else:
#                 heapq.heappush(q, (-d, -c))
#                 break
#         lst.sort(key=lambda x: x[1], reverse=True)
#         d, c = lst.pop(0)
#         #print(d, c,'dc')
#         total_cupramen_cnt += c
#         for d, c in lst:
#             heapq.heappush(q, (-d, -c))
#     else:
#         # 데드라인이 더 작은경우
#         heapq.heappush(q, (-deadline, -cupramen_cnt))
#     time -= 1
# print(total_cupramen_cnt)
    

# 실습 --- 2배럭 실패 (시간초과)
    
# time = max_deadline
# total_cupramen_cnt = 0
# while q and time > 0:
#     deadline, cupramen_cnt = heapq.heappop(q)
#     deadline *= -1; cupramen_cnt *= -1
#     #print(deadline, cupramen_cnt, time, total_cupramen_cnt, 'time')
#     if time <= deadline:
#         q2 = []
#         heapq.heappush(q2, (-cupramen_cnt, -deadline))
#         while q:
#             d, c = heapq.heappop(q)
#             #print(d, c,'asdf')
#             if time <= -d:
#                 heapq.heappush(q2, (c, d))
#             else:
#                 heapq.heappush(q, (d, c))
#                 break

#         #print(q2, '계산전 q2')
#         c, d = heapq.heappop(q2)
#         #print(c, d,'asdf2')
#         total_cupramen_cnt += -c
#         #print(q,'this is q')
#         # q = q+q2
        
#         while q2:
#             c, d = heapq.heappop(q2)
#             heapq.heappush(q, (d, c))
#         #print(q,'this is now q')
#     else:
#         # 데드라인이 더 작은경우
#         heapq.heappush(q, (-deadline, -cupramen_cnt))
#     #print()
#     time -= 1
# print(total_cupramen_cnt)
    
# 실습 --- 새로운 무언가 필요할때,, 조건내에서 최대값을 뽑아올때 궂이 우선순위큐 볼것없이 순회해서 찾은담에 그 값만  q.pop(index) 이런식으로 뽑아오는건 별론가?, 20퍼 시간초과 ,, 그래도 늘었다..
    
# time = max_deadline
# total_cupramen_cnt = 0
# while q and time > 0:
#     deadline, cupramen_cnt = heapq.heappop(q)
#     deadline *= -1; cupramen_cnt *= -1
#     #print(deadline, cupramen_cnt, time, total_cupramen_cnt, 'time')
#     if time <= deadline:
#         idx, deadline_flag, cupramen_cnt_flag = -1, deadline, cupramen_cnt
#         for i in range(len(q)):
#             deadline_, cupramen_cnt_ = q[i]
#             deadline_ *= -1; cupramen_cnt_ *= -1
#             if time <= deadline_:
#                 if cupramen_cnt_flag < cupramen_cnt_:
#                     cupramen_cnt_flag = cupramen_cnt_
#                     deadline_flag = deadline_
#                     idx = i
#                 elif cupramen_cnt_flag == cupramen_cnt_:
#                     if deadline_flag < deadline_:
#                         deadline_flag = deadline_
#                         idx = i

#         #print(q, 'qq')
#         if idx == -1:
#             total_cupramen_cnt += cupramen_cnt
#         else:
#             deadline_, cupramen_cnt_ = q.pop(idx)
#             total_cupramen_cnt += -1*cupramen_cnt_
#             heapq.heappush(q, (-deadline, -cupramen_cnt))
#     else:
#         # 데드라인이 더 작은경우
#         heapq.heappush(q, (-deadline, -cupramen_cnt))
#     #print()
#     time -= 1
# print(total_cupramen_cnt)


# 실습 -- 새로운 무언가가 또 필요하다 컵라면 크기로 정렬된 힙하나랑 데드라인 크기로 정렬된 힙하나


# import sys 
# import heapq
# input = sys.stdin.readline

# N = int(input())
# q = []
# q2 = []
# max_deadline = 0
# dic = {}
# for _ in range(N):
#     a, b = map(int, input().split())
#     max_deadline = max(a, max_deadline)
#     dic[a,b] = 1
#     heapq.heappush(q, (-a, -b)) # 데드라인이 큰게 먼저나옴, 데드라인이 같으면 컵라면 갯수가 많은게 먼저나온다
#     heapq.heappush(q2, (-b, -a)) # 컵라면 갯수가 큰게 먼저나옴, 데드라인도 큰게 먼저나와야 한다.

# # 어떻게 요리할것인가 컵라면 갯수가 큰녀석을 어떻게 제거 할것인가 visited를 만든다? 딕셔너리에 해당 값이 없으면 자연스레 다른 힙에서도 삭제

# time = max_deadline
# total_cupramen_cnt = 0
# while q and time > 0:
#     deadline, cupramen_cnt = heapq.heappop(q)
#     deadline *= -1; cupramen_cnt *= -1
#     #print(deadline, cupramen_cnt, time, total_cupramen_cnt, 'time')
#     if time <= deadline:
#         # 해당하는 값에서 가장 큰것을 뺀다
#         while q2 and dic[deadline, cupramen_cnt]:
#             cupramen_cnt2, deadline2 = heapq.heappop(q2)
#             cupramen_cnt2 *= -1; deadline2 *= -1
#             if time <= deadline2:


    
#     else:
#         # 데드라인이 더 작은경우
#         heapq.heappush(q, (-deadline, -cupramen_cnt))
#     #print()
#     time -= 1
# print(total_cupramen_cnt)

# 2시간 반만에 답 봄

import sys 
import heapq
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    deadline, cupramen_cnt = map(int, input().split())
    array.append((deadline, cupramen_cnt))

array.sort()
q = []
for deadline, cupramen_cnt in array:
    heapq.heappush(q, (cupramen_cnt))
    if deadline < len(q):
        heapq.heappop(q)

print(sum(q))