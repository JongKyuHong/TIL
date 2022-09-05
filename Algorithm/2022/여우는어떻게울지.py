import sys
input = sys.stdin.readline

for _ in range(int(input())):
    data = list(input().rstrip().split()) # 동물의 울음소리 최대 100글자
    answer = []
    sound = {}
    while 1:
        array_data = list(input().split())
        if len(array_data) == 5:
            answer = array_data
            break
        if array_data[2] in sound:
            sound[array_data[2]] += 1
        else:
            sound[array_data[2]] = 1
    
    for i in data:
        if i not in sound:
            print(i, end=' ')
