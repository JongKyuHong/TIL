from collections import deque
def solution(enroll, referral, seller, amount):
    answer = {}
    #parent = []*len(enroll)
    parent = {}
    for i in range(len(enroll)):
        answer[enroll[i]] = 0
        if referral[i] == '-':
            continue
        else:
            parent[enroll[i]] = referral[i]
    
    for i in range(len(seller)):
        s = seller[i]
        a = amount[i]
        q = deque()
        q.append((s,a))
        while q:
            s, a = q.popleft()
            if parent[s]:
                if a // 10 < 10:
                    answer[s] += a
                else:
                    ans = a//10
                    answer[s] += (a-ans)
                    answer[parent[s]] += ans
                    q.append((parent[s], ans))

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))