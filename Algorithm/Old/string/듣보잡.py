n,m = map(int,input().split())
array = [input() for _ in range(n)]
array2 = [input() for _ in range(m)]
new_list = list(set(array) & set(array2))
new_list.sort()
print(len(new_list))
for i in new_list:
    print(i)



