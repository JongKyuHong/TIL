import sys
input = sys.stdin.readline

N = int(input())
menu_nums = list(map(int, input().split()))
stickers = []
one_sticker = 0
max_sticker_cnt = 0
for i in menu_nums:
    if i not in stickers:
        stickers.append(i)
        one_sticker += 1
        max_sticker_cnt = max(max_sticker_cnt, one_sticker)
    else:
        one_sticker -= 1
print(max_sticker_cnt)