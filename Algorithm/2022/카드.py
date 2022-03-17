n = int(input())
dic = {}
val = []
for _ in range(n):
    a = int(input())
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

print(sorted(sorted(dic.items(),key=lambda x: x[0]), key=lambda x : x[1],reverse=True)[0][0])
