n = int(input())
people = list(map(int, input().split()))

board = [[] for _ in range(n)]
for i in range(n):
    x = list(map(int, input().split()))
    for j in x[1:]:
        board[i].append(j-1)