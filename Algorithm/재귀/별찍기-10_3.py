def append_star(len):
    if len == 1:
        return ['*']
    
    stars = append_star(len//3) # 9 3 1
    res = []
    for i in stars:
        res.append(i*3)
    for i in stars:
        res.append(i+' '*(len//3)+i)
    for i in stars:
        res.append(i*3)
    return res

n = int(input())
print('\n'.join(append_star(n)))