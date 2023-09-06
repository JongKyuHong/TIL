from collections import defaultdict
def solution(info, query):
    answer = []
    applicants = defaultdict(list)
    def made(lst, idx, val):
        if idx == 4:
            applicants[val].append(int(lst[idx]))
            return
        if lst[idx] == '-':
            made(lst, idx+1, val+'-')
        else:
            made(lst, idx+1, val+'-')
            made(lst, idx+1, val+lst[idx])
        
    for i in info:
        tmp = i.split()
        made(tmp, 0, '')
    for q in query:
        q = q.split()
        q, sc = q[:len(q)-1], int(q[-1])
        tmp = ''
        for i in q:
            if i == 'and':
                continue
            else:
                tmp += i
#        result = 0
        #print(tmp)
        applicants[tmp].sort()
        #print(applicants[tmp], sc)
        start, end = 0, len(applicants[tmp])-1
        while start <= end:
            mid = (start+end)//2
            #print(mid,'mid')
            if applicants[tmp][mid] >= sc:
                end = mid - 1
            elif applicants[tmp][mid] < sc:
                start = mid + 1
        #print(start,'end')
        answer.append(len(applicants[tmp]) - start)
            # else:
            #     # 같으면 같은게 몇개가 있는지도 봐야한다.
            #     idx = mid
            #     val = len(applicants[tmp]) - 1 - mid# 미드는 인덱스기 때문에
            #     print(val)
            #     while 1:
            #         idx -= 1
            #         if applicants[tmp][idx] == sc:
            #             val += 1
            #         else:
            #             break
            #     answer.append(val)
            #     break
#         for i in applicants[tmp]:
#             if i >= sc:
#                 result += 1
#        answer.append(result)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))