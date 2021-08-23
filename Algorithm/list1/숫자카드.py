t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    cards = input()
    count_card = {i : 0 for i in range(10)}
    for card in cards:
        card = int(card)
        count_card[card] += 1
    max_cnt = 0
    max_card = 0
    for card_num in range(9,-1,-1):
        if count_card[card_num] > max_cnt:
            max_cnt = count_card[card_num]
            max_card = card_num
    print(f'#{test_case} {max_card} {max_cnt}')
