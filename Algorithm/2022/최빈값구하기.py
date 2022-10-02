def solution(array):
    o_dict = {}
    for i in array:
        if i not in o_dict:
            o_dict[i] = 1
        else:
            o_dict[i] += 1
    print(o_dict)
    answer = []
    max_v = 0
    for k,v in o_dict.items():
        if v > max_v:
            answer = [k]
            max_v = v
        elif v == max_v:
            answer.append(k)
    return -1 if len(answer) > 1 or not answer else max_v

print(solution([]))
#print(solution([1,1,2,2,3,3,4,5,6]))