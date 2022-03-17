from itertools import combinations
import math
def solution(nums):
    answer = 0
    for i in combinations(nums,3):
        flag = 1
        a = sum(i)
        for j in range(2,int(math.sqrt(a))+1):
            if a % j == 0:
                flag = 0
                break
        if flag:
            answer += 1
    return answer

print(solution([1,2,3,4]))