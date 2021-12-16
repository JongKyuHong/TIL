from collections import Counter
def solution(str1, str2):
    list1, list2 = [], []
    for i in range(len(str1)-1):
        list1.append(str1[i].lower()+str1[i+1].lower())
    for i in range(len(str2)-1):
        list2.append(str2[i].lower()+str2[i+1].lower())
    
    list1 = Counter(list1)
    list2 = Counter(list2)
    a, b = [], []
    for i in list1:
        if i.isalpha():
            a_val = min(list1[i],list2[i])
            b_val = max(list1[i],list2[i])
            for _ in range(a_val):
                a.append(i)
            for _ in range(b_val):
                b.append(i)
    for i in list2:
        if i.isalpha() and i not in b:
            b_val = max(list1[i],list2[i])
            for _ in range(b_val):
                b.append(i)
    
    if not b and not a:
        return 65536
    else:
        return int((len(a)/len(b))*65536)

print(solution('FRANCE','french'))