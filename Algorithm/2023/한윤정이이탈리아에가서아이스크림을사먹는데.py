import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mix = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    mix[a].append(b)
    mix[b].append(a)
lst = []
cnt = 0
def makeicecream(arr, length, standard):
    if length == 3:
        global cnt
        cnt += 1
        return
    for i in range(1, N+1):
        if i not in arr and standard < i:
            flag = 0
            for j in arr:
                if j in mix[i]:
                    flag += 1
                    break
            if not flag:
                makeicecream(arr+[i],length+1, i)
    
for i in range(1, N+1):
    makeicecream([i], 1, i)
print(cnt)