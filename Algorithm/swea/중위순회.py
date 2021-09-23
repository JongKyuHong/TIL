def inorder(index):
    temp = ''
    if index*2 < len(nodes):
        temp += inorder(index*2)
    temp += nodes[index]
    if index*2+1 < len(nodes):
        temp += inorder(index*2+1)
    return temp

for test_case in range(10):
    n = int(input())
    nodes = [0] * (n+1)
    for _ in range(n):
        input_data = list(input().split())
        nodes[int(input_data[0])] = input_data[1]
    res = inorder(1)
    print(f'#{test_case+1} {res}')