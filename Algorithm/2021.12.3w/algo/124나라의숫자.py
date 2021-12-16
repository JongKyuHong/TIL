def solution(n):
    nums = [1,2,4]
    answer =''
    while n > 0:
        n -= 1
        answer = str(nums[n%3]) + answer
        n //= 3
    return answer

def solution2(n):
    nums = [1, 2, 4]
    answer = ''
    while (n > 0):
        n -= 1
        answer = str(nums[n % 3]) + answer
        n = n // 3
    return answer
print(solution2(15))