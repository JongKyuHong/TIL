import sys
from collections import Counter

s = list(map(str, sys.stdin.readline().strip()))
S = Counter(s)

def find(tmp, length):
    ans = 0
    if length == len(s):
        return 1

    for k in S.keys():
        if k == tmp or S[k] == 0:
            continue

        S[k] -= 1
        ans += find(k, length + 1)
        S[k] += 1
        
    return ans

print(find('', 0))