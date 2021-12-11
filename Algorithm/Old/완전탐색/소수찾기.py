from itertools import permutations

def check(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for i in range(1,len(numbers)+1):
        perlist = list(map(''.join,permutations(list(numbers),i)))
        for k in list(set(perlist)):
            if check(int(k)):
                answer.append(int(k))
    answer = len(set(answer))
    return answer

print(solution("17"))




