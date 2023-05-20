import sys
input = sys.stdin.readline

input_ = input().rstrip()
gap = 1
while gap < len(input_):
    idx = 0
    start = input_[idx:idx+gap]
    flag = 0
    while idx+gap < len(input_):
        if int(input_[idx:idx+gap])+1 == int(input_[idx+gap:idx+gap+len(str(int(input_[idx:idx+gap]) + 1))]):
            if gap != len(str(int(input_[idx:idx+gap]) + 1)):
                tmp = gap
                gap = len(str(int(input_[idx:idx+gap]) + 1))
                idx += len(input_[idx:idx+tmp])
            else:
                idx += len(input_[idx:idx+gap])
        else:
            flag = 1
            break
    if not flag:
        print(int(start), int(input_[idx:idx+gap]))
        exit()
    else:
        gap += 1
if gap == len(input_):
    print(input_, input_)
