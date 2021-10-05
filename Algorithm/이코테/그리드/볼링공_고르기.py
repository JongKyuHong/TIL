n, m = map(int, input().split()) # n 공의 갯수, m 공의 최대무게
bowling = list(map(int, input().split()))
index = 0
player1 = 0
new_list = []
while index < n:
    player1 = bowling[index]
    for i in range(index+1, n):
        if player1 != bowling[i]:
            new_list.append(f'{player1}{bowling[i]}')
    index += 1
print(len(new_list))
    





