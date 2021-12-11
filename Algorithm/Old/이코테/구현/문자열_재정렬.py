input_data = input()
nums = []
string = []
for i in input_data:
    if i.isdigit():
        nums.append(int(i))
    else:
        string.append(i)
string.sort()
print(''.join(string)+str(sum(nums)))