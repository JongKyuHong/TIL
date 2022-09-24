from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    limit = 2*(len(q1)+len(q2))
    cnt = 0
    
    if (sum_q1 + sum_q2) % 2:
        return -1
    
    while limit > cnt:
        if sum_q1 == sum_q2:
            return cnt
        if sum_q1 > sum_q2:
            qp = q1.popleft()
            q2.append(qp)
            sum_q1 -= qp
            sum_q2 += qp
        else:
            qp = q2.popleft()
            q1.append(qp)
            sum_q2 -= qp
            sum_q1 += qp
        cnt += 1
        
    return -1