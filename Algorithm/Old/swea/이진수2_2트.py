def change_bin(nums):
    step = 0
    result = ''
    while nums:
        ans2 = nums * 2
        result += str(int(ans2))
        if int(ans2) == 0:
            nums = ans2
        else:
            nums = ans2 - int(ans2)
        step += 1
        if step > 12:
            return 'overflow'
    return result

for test_case in range(int(input())):
    n = float(input())
    print(f'#{test_case+1} {change_bin(n)}')