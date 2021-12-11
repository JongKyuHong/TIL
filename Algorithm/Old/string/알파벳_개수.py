s = input()
array = [0]*26
for i in s:
    array[ord(i)-ord('a')] += 1
print(*array)



