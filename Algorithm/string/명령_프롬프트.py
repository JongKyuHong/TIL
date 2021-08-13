import sys

n = int(sys.stdin.readline())
file_name_list = []

for i in range(n):
    file_name_list.append(sys.stdin.readline().rstrip())

pattern = list(file_name_list[0])

for file_name in file_name_list[1:]:
    for i in range(len(file_name)):
        if pattern[i] == '?':
            pass
        elif pattern[i] != file_name[i]:
            pattern[i] = '?'
print(''.join(pattern))