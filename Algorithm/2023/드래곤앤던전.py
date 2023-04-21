import sys
input = sys.stdin.readline

def can_clear(curATK, maxHP):
    curHP = maxHP
    for t, atk, hp in lst:
        if t == 1:
            turn = hp//curATK if not hp % curATK else hp//curATK + 1
            curHP -= atk*(turn-1)
        else:
            curATK += atk
            curHP += hp
            if curHP > maxHP:
                curHP = maxHP
        if curHP <= 0:
            return False
    return True

N, H = map(int, input().split())
lst = []
for _ in range(N):
    t, a, h = map(int, input().split()) # a공격력 h생명력
    lst.append([t,a,h])

result = 0
start, end = 1, N*1000000*1000000
while start <= end:
    mid = (start+end)//2
    if can_clear(H, mid):
        end = mid - 1
        result = mid
    else:
        start = mid + 1
print(result)