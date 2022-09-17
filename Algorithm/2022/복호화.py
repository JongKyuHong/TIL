for _ in range(int(input())):
    data = list(input())
    words = {}
    for i in data:
        if i.isalpha():
            if i not in words:
                words[i] = 1
            else:
                words[i] += 1
    mw,value, value_cnt = '',-1,0
    for k,v in words.items():
        if v > value:
            value_cnt = 0
            value = v
            mw = k
        elif v == value:
            value_cnt += 1
    if value_cnt > 0:
        print("?")
    else:
        print(mw)
        
