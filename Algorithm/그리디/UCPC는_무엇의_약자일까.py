new_data = input()

check = 0
ch_u = 0
for j in new_data:
    if j == 'U' and ch_u == 0:
        check += 1
        ch_u += 1
    elif j == 'C' and check == 1:
        check += 1
    elif j == 'P' and check == 2:
        check += 1
    elif j == 'C' and check == 3:
        check += 1
if check == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')
