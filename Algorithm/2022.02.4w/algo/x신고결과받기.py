def solution(id_list, report, k):
    answer = [0]*len(id_list)
    
    dic_report = {id : [] for id in id_list}
    for re in set(report):
        r = re.split(' ')
        dic_report[r[1]].append(r[0])
    
    for key, value in dic_report.items():
        if len(value) >= k:
            for v in value:
                answer[id_list.index(v)] += 1
                

                
    return answer
print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))