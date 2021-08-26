from collections import deque

for test_case in range(int(input())):
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))
    que = deque([])
    pizza = deque(pizza)
    i = 0
    while n != i:
        que.append([pizza.popleft(), i])
        i += 1
    
    while len(que) > 1:
        cheese, index = que.popleft()
        cheese //= 2
        if cheese == 0:
            if pizza:
                que.append([pizza.popleft(), i])
                i += 1
        else:
            que.append([cheese, index])
    
    print(f'#{test_case+1} {que[0][1]+1}')
                
