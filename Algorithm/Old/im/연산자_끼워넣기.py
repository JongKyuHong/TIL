n = int(input())
array = list(map(int, input().split()))
numbers = list(map(int, input().split()))
maximum = -1e9
minimum= 1e9
def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    
    if plus:
        dfs(depth+1, total + array[depth],plus -1,minus, multiply, divide)
    if minus:
        dfs(depth+1, total - array[depth],plus , minus-1 , multiply, divide)
    if multiply:
        dfs(depth+1, total * array[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total / array[depth]),plus,minus, multiply, divide-1)


dfs(1, array[0], numbers[0], numbers[1], numbers[2], numbers[3])
print(maximum)
print(minimum)




