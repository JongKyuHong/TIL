import sys
input = sys.stdin.readline

data = input().rstrip()
if ' ' in data:
    print('Error!')
    exit()

if '_' in data: # C++ 일때, _를 삭제 그리고 _ 다음문자 대문자로 변경
    if data[-1] == '_':
        print('Error!')
        exit()
    new_data = ''
    flag = 0
    for i in data:
        if i.isupper():
            print('Error!')
            exit()
        if i == '_':
            if flag == 1:
                print('Error!')
                exit()
            else:
                flag = 1
        else:
            if flag == 1:
                flag = 0
                new_data += i.upper()
            else:
                new_data += i
    print(new_data)
else: # java일때, 대문자를 만나면 그앞에 _추가
    if data[0].isupper():
        print('Error!')
        exit()
    new_data = ''
    flag = 0
    for i in data:
        if i.isupper():
            new_data += '_'+i.lower()
        else:
            new_data += i
    print(new_data)