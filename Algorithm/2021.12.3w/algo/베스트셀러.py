n = int(input())
dic = {}
for _ in range(n):
    book = input()
    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1
print(sorted(sorted(dic.items()),key=lambda x: x[1],reverse=True)[0])