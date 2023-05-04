from collections import defaultdict
import sys
input = sys.stdin.readline

card = []
cards = defaultdict(int)
nums = defaultdict(int)
for _ in range(5):
    a, b = input().rstrip().split()
    b = int(b)
    cards[a] += 1
    nums[b] += 1
    card.append((a, b))

cards_list = sorted(cards.items(), key=lambda x: x[1], reverse=True)
card_list = sorted(card, key=lambda x: x[1], reverse=True)
nums_list = sorted(nums.items(), key=lambda x: (x[1],x[0]), reverse=True)
# 1. 카드 5장이 모두 같은색이고 연속된 숫자. 가장 높은 숫자에 +900

# 4. 카드 5장이 모두 같은색. 가장 높은 숫자에 +600
for k, v in cards_list:
    if v == 5:
        prev = -1
        flag = 0
        for card_name, card_value in card_list:
            if prev == -1:
                prev = card_value
            else:
                if prev - 1 == card_value:
                    prev = card_value
                else:
                    flag = 1
                    break
        if flag:
            print(card_list[0][1]+600)
        else:
            print(card_list[0][1]+900)
        exit()

if len(nums_list) == 2:
    # 2. 카드 4장이 모두 같은색이다. 가장 높은 숫자에 +800
    if nums_list[0][1] == 4:
        print(nums_list[0][0]+800)
        exit()
    # 3. 3장숫자 같고 2장숫자 같다
    elif nums_list[0][1] == 3 and nums_list[1][1] == 2:
        print(nums_list[0][0]*10 + nums_list[1][0] + 700)
        exit()
elif len(nums_list) == 3:
    if nums_list[0][1] == 3: # 6. 카드 5장중 3장의 숫자가 같다
        print(nums_list[0][0]+400)
        exit()
    elif nums_list[0][1] == 2 and nums_list[1][1] == 2: # 7. 카드 5장중 2장의 숫자가 같고 또 다른 2장의 숫자가 같을때 
        print(nums_list[0][0]*10 + nums_list[1][0] + 300)
        exit()
elif len(nums_list) == 4:
    if nums_list[0][1] == 2: # 8. 카드 5장중 2장의 숫자가 같을때
        print(nums_list[0][0]+200)
        exit()

# 5. 카드 5장 숫자 연속
prev = -1
flag = 0
for card_name, card_value in card_list:
    if prev == -1:
        prev = card_value
    else:
        if prev - 1 == card_value:
            prev = card_value
        else:
            flag = 1
            break
if flag:
    print(card_list[0][1] + 100) # 9. 어떤 경우에도 해당되지 않을때
else:
    print(card_list[0][1]+500)



