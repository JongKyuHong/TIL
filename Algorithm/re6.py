def make_tree(parent, res):
    if tree[parent]:
        for i in tree[parent]:
            if i == 0:
                continue
            visited[parent] += 1
            if visited[parent] > 1:
                print(res)
                res2 = '-'
                res = res2*(len(res)-3)
            res += f'{i} '
            make_tree(i, res)
        if visited[parent] >= 1:
            print(res)
    return

numbers = list(map(int, input().split()))
tree = [[0] for _ in range(1000)]
visited = [0] * 1000
for i in range(0,len(numbers)-1,2):
    tree[numbers[i]].append(numbers[i+1])
res = f'{numbers[0]} '
make_tree(numbers[0], res)



