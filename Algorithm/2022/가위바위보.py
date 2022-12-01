import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    robots = [input().rstrip() for _ in range(n)]
    len_robot = len(robots[0])
    idx = 0
    while idx < len_robot:
        s,r,p = '','',''
        for i in range(n):
            if robots[i]:
                if robots[i][idx] == 'S':
                    s += str(i)
                elif robots[i][idx] == 'R':
                    r += str(i)
                else:
                    p += str(i)
        if s and r and not p:
            for i in s:
                robots[int(i)] = []
        elif r and p and not s:
            for i in r:
                robots[int(i)] = []
        elif p and s and not r:
            for i in p:
                robots[int(i)] = []
        idx += 1

    ans = []
    for i in range(n):
        if robots[i]:
            ans.append(i)

    if len(ans) == 1:
        print(ans[0]+1)
    else:
        print(0)