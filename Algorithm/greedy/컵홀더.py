n = int(input())

people = input()
array = []
if people[0] == 'L':
    array.append('*')
    array.append('L')
elif people[0] == 'S':
    array.append('*')
    array.append('S')
    array.append('*')
for i in range(1,len(people)):
    if people[i] == 'S':
        array.append('S')
        array.append('*')
    elif people[i] == 'L':
        if array[-1] == 'L':
            array.append('L')
            array.append('*')
        elif array[-1] == '*':
            array.append('L')
if array.count('*') > n:
    print(n)
else:
    print(array.count('*'))
