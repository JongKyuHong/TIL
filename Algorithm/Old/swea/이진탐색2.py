def make_tree(index):
    global cnt
    if index <= n:
        make_tree(index*2)
        tree[index] = cnt
        cnt += 1
        make_tree(index*2 + 1)
    
for test_case in range(int(input())):
    n = int(input())
    cnt = 1
    tree = [0 for i in range(n+1)]
    make_tree(1)
    print(f'#{test_case+1} {tree[1]} {tree[n//2]}')