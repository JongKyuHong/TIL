def solution(nums):
    target = len(nums)//2
    answer = 0
    nums_len = len(set(nums))
    if target < nums_len:
        answer = target
    else:
        answer = nums_len
    return answer

print(solution([3,1,2,3]))