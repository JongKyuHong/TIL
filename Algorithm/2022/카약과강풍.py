import sys
input = sys.stdin.readline

n, s, r = map(int, input().split()) # 팀의수, 카약이 손상된 팀의수, 하나 더 가져온 팀의 수
s_lst = list(map(int, input().split())) # 카약이 손상된 팀
r_lst = list(map(int, input().split())) # 하나 더 가져온 팀

for r in r_lst:
    if r in s_lst:
        s_lst.remove(r)
    elif r-1 in s_lst:
        s_lst.remove(r-1)
    elif r+1 in s_lst:
        s_lst.remove(r+1)
    
print(len(s_lst))