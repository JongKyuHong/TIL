a,b = map(int,input().split()) #  현재주파수a , 듣고싶은 주파수b이다.
n = int(input()) # 주파수 즐찾버튼?
array = []
for _ in range(n):
    array.append(int(input()))

for i in range(n):
    if array[i] == b:
        print(1)
        exit(0)
array.append(b)
array.sort()
if len(array) >= 3:
    b_index = array.index(b)
    b_under = b - array[b_index-1]
    b_over = array[b_index+1] -b

    if abs(b - b_under) > abs(a-b) and abs(b_over - b) > abs(a-b):
        print(abs(a-b))
    else:
        if  abs(b_under) > abs(b_over):
            print(abs(b_over)+1)
            exit(0)
        else:
            print(abs(b_under)+1)
            exit(0)
else:
    b_index = array.index(b)
    if b_index == 0:
        if array[b_index+1] - b>abs(a-b):
            print(abs(a-b))
        else:
            print(array[b_index+1] - b + 1)
    else:
        if  b - array[b_index-1] >abs(a-b):
            print(abs(a-b))
        else:
            print(b - array[b_index-1] +1)