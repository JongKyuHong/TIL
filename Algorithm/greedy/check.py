def lonely(list):
    dw = 0
    new_list = []
    for i in list:
        if dw == i:
            continue
        else:
            new_list.append(i)
            dw=i
    return new_list
            

    
print(lonely([1,1,3,3,0,1,1]))
print(lonely([4,4,4,3,3]))