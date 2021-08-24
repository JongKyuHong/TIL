from _typeshed import StrPath


t = int(input())


def r(start,end):
    if cards[start] > cards[end]:
        if cards[start] == 3 and cards[end] == 1:
            return end
        else:
            return start
    elif cards[start] < cards[end]:
        if cards[end] == 3 and cards[start] == 1:
            return start
        else:
            return end
    else:
        return start




def check(start,end):
    if start == end:
        return start
    else:
        a = check(start,(start+end)//2)
        b = check(((start+end)//2)+1,end)
        return r(a,b)           


for test_case in range(1,t+1):
    n = int(input())
    cards = list(map(int,input().split()))
    stack = []
    for idx, val in enumerate(cards):
        stack.append([idx,val])
    ans = check(0,n-1)+1



