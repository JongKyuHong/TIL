def dfs(index):
    global minAns
    if index == n // 2:
        startSum = 0
        linkSum = 0
        for i in range(0, n):
            if i not in start:
                link.append(i)
        for i in range(0, n//2 -1):
            for j in range(i+1, n// 2):
                startSum += arr[start[i]][start[j]] + arr[start[j]][start[i]]
                linkSum += arr[link[i]][link[j]] + arr[link[j]][link[i]]
        diff = abs(linkSum - startSum)
        if minAns > diff:
            minAns = diff
        link.clear()
        return
    for i in range(n):
        if i in start:
            continue
        if len(start) > 0 and start[len(start)-1]> i:
            continue
        start.append(i)
        dfs(index+1)
        start.pop() 


n = int(input())
arr = []
start= []
link = []
for i in range(n):
    arr.append(list(map(int, input().split())))
minAns = float('inf')
dfs(0)
print(minAns)
#https://kyun2da.github.io/2020/08/11/startandlink/

