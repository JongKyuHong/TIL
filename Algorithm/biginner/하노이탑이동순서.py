def hanoi(n,a,b,c):
    if n == 1:
        move.append([a,c])  # 1이면 그냥 a에서 c로옮김
    else:
        hanoi(n-1,a,b,c)  # a에서 c로가는게임인데 얘네는 2로 가있는다생각
        move.append([a,c])  # a에서 c로 옮김
        hanoi(n-1,b,a,c)  # 2에있던 n-1개를 c위로 보냄

k = int(input())

move = []
hanoi(k,1,2,3) # 입력받은 k와 1번2번3번 발판

print(len(move))
print('\n'.join([' '.join(str(i) for i in row) for row in move]))
