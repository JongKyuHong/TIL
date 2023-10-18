import sys 
input = sys.stdin.readline

def check(tmp):
    flag1, flag2 = 0, 0
    for t in tmp:
        if t in ['a', 'e', 'i', 'o', 'u']:
            flag1 += 1
        else:
            flag2 += 1
    if flag1 >= 1 and flag2 >= 2:
        return True
    return False


def find(target):
    if len(target) == L:
        if check(target):
            answer.append(''.join(target))
    else:
        for l in lst:
            if target == '' or ord(target[-1]) < ord(l):
                find(target + l)

L, C = map(int, input().split())
lst = list(input().split())
lst.sort()
answer = []
find('')
answer.sort()
for a in answer:
    print(a)

