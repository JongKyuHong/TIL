def solution(topping):
    answer = 0
    res = []
    for i in topping:
        if i not in res:
            res.append(i)
    idx = len(res)
    lst = {}
    lst2 = {}
    for i in range(idx):
        if topping[i] not in lst:
            lst[topping[i]] = 1
        else:
            lst[topping[i]] += 1
    
    for i in range(idx, len(topping)):
        if topping[i] not in lst2:
            lst2[topping[i]] = 1
        else:
            lst2[topping[i]] += 1

    while idx < len(topping):
        print(lst, lst2)
        lst_answer = 0
        lst2_answer = 0
        for k, v in lst.items():
            if v >= 1:
                lst_answer += 1
        for k, v in lst2.items():
            if v >= 1:
                lst2_answer += 1
        if lst_answer == lst2_answer:
            answer += 1

        target = topping[idx]
        if target not in lst:
            lst[target] = 1
        else:
            lst[target] += 1
        lst2[target] -= 1
        
        
        
        idx += 1
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))