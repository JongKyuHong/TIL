n = int(input())
a = list(input().split())
def check(location):
    if location[0] <= 0 or location[0] > n or location[1] <= 0 or location[1] > n:
        return False
    return True 
location = [1,1]
for i in range(len(a)):
    if a[i] == 'L':
        location[0] -= 1
        if check(location) == False:
            location[0] += 1
    elif a[i] == 'R':
        location[0] += 1
        if check(location) == False:
            location[0] -= 1
    elif a[i] == 'U':
        location[1] -= 1
        if check(location) == False:
            location[1] += 1
    elif a[i] == 'D':
        location[1] += 1
        if check(location) == False:
            location[1] -= 1
    else:
        print("입력을 잘못하셨습니다.")
        break
print(location[1], location[0])



