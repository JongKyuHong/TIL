def check_baby(player, index):
    global res
    if player % 2:
        if player1_nums[index] == 3:
            res = 1
        elif index < 8 and player1_nums[index] and player1_nums[index+1] and player1_nums[index+2]:
            res = 1
        elif index > 1 and player1_nums[index] and player1_nums[index-1] and player1_nums[index-2]:
            res = 1
        elif 0 < index < 9 and player1_nums[index] and player1_nums[index+1] and player1_nums[index-1]:
            res = 1
    else:
        if player2_nums[index] == 3:
            res = 2
        elif index < 8 and player2_nums[index] and player2_nums[index+1] and player2_nums[index+2]:
            res = 2
        elif index > 1 and player2_nums[index] and player2_nums[index-1] and player2_nums[index-2]:
            res = 2
        elif 0 < index < 9 and player2_nums[index] and player2_nums[index+1] and player2_nums[index-1]:
            res = 2


for test_case in range(int(input())):
    nums = list(map(int, input().split()))
    player1_nums = [0] * 10
    player2_nums = [0] * 10
    res = 0
    for i in range(12):
        if i % 2:
            player2_nums[nums[i]] += 1
            if i >= 4:
                check_baby(2, nums[i])
        else:
            player1_nums[nums[i]] += 1
            if i >= 4:
                check_baby(1, nums[i])
        if res:
            break
    print(f'#{test_case+1} {res}')
            