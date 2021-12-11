import sys

# N: 예선 참가자 수, M: 장르, K: 본선 진출자 수
N, M, K = map(int, sys.stdin.readline().split())

candidate_score = {}
for i in range(N):
    candidate_score[i+1] = 0

for i in range(M):
    genre = list(map(float, sys.stdin.readline().split()))
    for j in range(0, 2*N, 2):
        if genre[j+1] > candidate_score[genre[j]]:
            candidate_score[genre[j]] = genre[j+1]
new_dict = sorted(list(candidate_score.values()),reverse=True)
sum1 = sum(new_dict[:K])
print('%.1f'%sum1)
# result = 0
# for i in new_dict:
#     if k == 0:
#         break
#     else:
#         result += i
# print(result)


#array.sort(key=lambda x:x[1],reverse=True)
# for i in array:
#     #print(i) # ['2', '3.0', '1', '0.2', '3', '0.1'], ['3', '1.0', '2', '0.5', '1', '0.2']
#     for j in range(0,len(i),2):
#         print(i[j])# 2,1,3 ,,, 3 2 1

    
