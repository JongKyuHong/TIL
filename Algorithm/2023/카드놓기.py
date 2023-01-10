from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
skills = list(map(int, input().split()))
skills.reverse()
cards = deque([i for i in range(1, N+1)])
cards.reverse()
ans = deque([])
for skill in skills:
    if skill == 1:
        ans.append(cards.pop())
    elif skill == 2:
        ans.insert(-1, cards.pop())
    else:
        ans.appendleft(cards.pop())
ans.reverse()
print(*ans)