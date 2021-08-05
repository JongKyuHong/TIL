n = int(input()) # 선수숫자
array = list(map(int,input().split())) #선수들
count = 0

while 1:
    maxa = max(array)
    lowest = array.index(maxa)
    num = len(array)

    if num == 1:
        print(count)
        break
    if lowest==0:
        gap = array[lowest]-array[lowest+1]
    elif lowest==(num-1):
        gap = array[lowest] - array[lowest-1]
    else:
        if array[lowest-1] > array[lowest+1]:
            gap = array[lowest]-array[lowest-1]
        else:
            gap = array[lowest]-array[lowest+1]
    count += gap
    array.pop(lowest)