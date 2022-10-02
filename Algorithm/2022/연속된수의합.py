def solution(num, total):
    left = 1
    center = total//num
    if num == 1:
        return [total]
    cnt = 1
    sum_v = center
    left = center - 1
    right = center + 1
    while 1:
        print(left, right)
        if num == cnt:
            if sum_v == total:
                break
            elif sum_v > total:
                sum_v -= right-1
                cnt -= 1
            else:
                sum_v -= left+1
                cnt -= 1
        if cnt % 2:
            sum_v += left
            left -= 1
        else:
            sum_v += right
            right += 1
        cnt += 1
    
    res = []
    for i in range(left+1, right):
        res.append(i)
    return res

print(solution(4,14))