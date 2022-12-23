import sys
input = sys.stdin.readline

n = int(input()) # 명령어 갯수
words = sorted([input().rstrip() for _ in range(n)], key=lambda x: len(x))
cnt = 0
for i in range(n):
    grand_flag = 0
    for j in range(i+1, n):
        flag = 0
        for l in range(len(words[i])):
            if words[i][l] != words[j][l]:
                flag = 1
                break
        if not flag:
            grand_flag = 1
            break
    if not grand_flag:
        #print(words[i],'a')
        cnt += 1
    
print(cnt)