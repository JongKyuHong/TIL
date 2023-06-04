from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
    flag = 0
    q = deque(list(input().rstrip()))
    for word in words:
        if ''.join(q) in word:
            flag = 1
            break
    if flag:
        continue
    w = []
    for _ in range(len(q)):
        q.rotate(1)
        w.append(''.join(list(q)))
    words.append(w)
print(len(words))