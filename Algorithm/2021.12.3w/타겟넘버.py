from collections import deque
def solution(numbers, target):
    ans = 0
    q = deque()
    n = len=(numbers)
    q.append([numbers[0],0])
    q.append([-1*numbers[0],0])