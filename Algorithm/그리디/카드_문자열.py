t = int(input())
for _ in range(t):
    n = int(input())
    array = list(input().split())
    ans = [array[0]]
    for i in range(1,len(array)):
        left = ans[0]
        right = ans[-1]
        if array[i] <= left:
            ans.insert(0,array[i])
        else:
            ans.append(array[i])
    print(''.join(ans))