from collections import deque
def solution(order):
    answer = 0
    A = deque(list(range(1, len(order)+1)))
    idx = 0
    tmp = []
    while A and idx < len(order):
        if order[idx] != A[0]:
            tmp.append(A.popleft())
        else:
            tmp.append(A.popleft())
            while tmp:
                if order[idx] == tmp[-1]:
                    answer += 1
                    tmp.pop()
                    idx += 1
                else:
                    break
            
            
    return answer

print(solution([4,3,1,2,5]))
print(solution([5,4,3,2,1]))