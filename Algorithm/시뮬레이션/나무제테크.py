import sys 
input = sys.stdin.readline
delta = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
lst = [[5]*N for _ in range(N)]
trees = [list(map(int, input().split())) for _ in range(M)] # x, y, 나무의 나이
trees.sort(key = lambda x: x[2])
tree = [[[] for _ in range(N)] for _ in range(N)]

for idx in range(K):
    deadtrees = []
    if idx == 0:
        for x, y, age in trees:
            x -= 1; y -= 1
            if lst[x][y] >= age: # 봄
                lst[x][y] -= age
                tree[x][y].append(age+1) # 최초니까 그냥 안넣어버림
            else:
                deadtrees.append([x, y, age])
    else:
        for i in range(N):
            for j in range(N):
                if tree[i][j]:
                    tree[i][j].sort()
                    len_tree = len(tree[i][j])
                    idx2 = 0
                    while idx2 < len_tree:
                        if lst[i][j] >= tree[i][j][idx2]:
                            lst[i][j] -= tree[i][j][idx2]
                            tree[i][j][idx2] += 1
                            idx2 += 1
                        else: # 넘지 못하면 이 뒤로는 사실 볼필요가 없다.
                            break
                    for _ in range(len_tree-idx2):
                        deadtrees.append([i, j, tree[i][j].pop()])

    for x, y, age in deadtrees: # 여름
        lst[x][y] += age//2



    # 가을
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                for k in tree[i][j]:
                    if k == 0:
                        continue
                    if k % 5 == 0:
                        for dr, dc in delta:
                            nr, nc = dr+i, dc+j
                            if 0 <= nr < N and 0 <= nc < N:
                                tree[nr][nc].append(1) # 새로운 나무 생성

    # 겨울
    for i in range(1, N+1):
        for j in range(1, N+1):
            lst[i-1][j-1] += A[i-1][j-1]
        
answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])
print(answer)



