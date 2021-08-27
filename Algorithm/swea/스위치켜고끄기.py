n = int(input())  # 스위치 개수
state = list(map(int,input().split()))  # 스위치의 상태
student = int(input())  # 학생수
stu_info = [list(map(int, input().split())) for _ in range(student)]  # 남학생은 1, 여학생은 2

for s, n1 in stu_info:
    if s == 1:
        for i in range(n1-1,n,n1):
            state[i] = -1*(state[i] - 1)
            
    else:
        n1 -= 1
        state[n1] = -1*(state[n1] - 1)
        index = 1
        while 1:
            if n1 + index >= n or n1 - index < 0:
                break
            else:
                if state[n1+index] == state[n1-index]:
                    state[n1+index] = -1*(state[n1+index] - 1)
                    state[n1-index] = -1*(state[n1-index] - 1)
                else:
                    break
            index += 1

for i in range(n):
    if i != 0 and i % 19 == 0:
        print(state[i])
    else:
        print(state[i],end=' ')

    
