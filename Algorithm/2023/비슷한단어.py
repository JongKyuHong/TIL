import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        visited1 = [0]*26
        visited2 = [0]*26
        flag = 1
        for k in range(len(words[j])):
            idx1 = ord(words[i][k]) - ord('a')
            idx2 = ord(words[j][k]) - ord('a')
            if visited1[idx1] == 0 and visited2[idx2] == 0:
                visited1[idx1] = words[j][k]
                visited2[idx2] = words[i][k]
            elif visited1[idx1] != words[j][k]:
                flag = 0
                break
        if flag:
            cnt += 1
print(cnt)