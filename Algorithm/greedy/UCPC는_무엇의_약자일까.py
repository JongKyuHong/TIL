id = input()
new_data = ''
check = 0
for i in id:
    if i.isupper():
        new_data += i

for j in new_data:
    if j == 'U':
        check += 1
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
