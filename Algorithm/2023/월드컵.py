import sys
input = sys.stdin.readline

def dfs(i, our_team):
    w, d, l = our_team
    if i == 6:
        if w == 0 and d == 0 and l == 0:
            
    
    win, draw, lose = team[i]
    if w and lose:
        w -= 1
    if d and draw:
        d -= 1
    if l and win:
        l -= 1
      

for _ in range(4):
    lst = list(map(int, input().split()))
    team = []
    for i in range(0, 18, 3):
        team.append([lst[i],lst[i+1],lst[i+2]])
    
    for i in range(6):
        dfs(i+1, team[i][:])