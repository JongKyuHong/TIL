import sys
import math
input = sys.stdin.readline

for _ in range(int(input())):
    word = input().rstrip()
    len_word = len(word)
    n = int(math.sqrt(len_word))
    graph = [['']*n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(n):
            graph[i][j] = word[idx]
            idx += 1
    target = ''
    for i in range(n-1,-1,-1):
        for j in range(n):
            target += graph[j][i]
    print(target)