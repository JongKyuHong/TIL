import sys
input = sys.stdin.readline

lst = input().rstrip()
lst = lst.split()
common = lst[0]
for string in lst[1:]:
    tmp = ''
    len_str = len(string[:-1])
    idx = len_str-1
    alpha = ''
    while idx >= 0:
        if string[idx] == ']':
            tmp += '[]'
            idx -= 2
        else:
            if string[idx].isalpha():
                alpha = string[idx] + alpha
                idx -= 1
            else:
                tmp += string[idx]
                idx -= 1
    
    print(common + tmp + ' ' + alpha +';')

