import math

def solution(numbers,target):
    sup = [0]
    for i in numbers:
        sub = []
        for j in sup:
            sub.append(i+1)
            sub.append(i-1)
        sup = sub
    return sub.count(target)

print(solution([1, 1, 1, 1, 1],3))