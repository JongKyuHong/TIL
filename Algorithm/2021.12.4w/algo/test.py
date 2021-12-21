alpha = input()
for i in alpha:
    if ord(i)-3 < ord('A'):
        val = ord('Z') - ord(i) + 3
    else:
        val = ord(i)-3
    print(chr(val),end='')