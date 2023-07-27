import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

if len(lst) % 2: 
    idx = len(lst)//2 # 같은 수가 반복 되어야 함 크기
else:
    idx2 = len(lst)//2
    idx1 = idx2-1


