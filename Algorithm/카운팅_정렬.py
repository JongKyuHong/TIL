열 우선순회
n x m 배열의 n,m원소를 빠짐없이 조사하는 방법
i 행의좌표
j 열의좌표

# 행우선순회
for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j]

# 열 우선순회
for j in range(len(array[0])):
    for i in range(len(array)):
        array[i][j]

# 지그재그 순회
for i in range(len(array)):
    for j in range(len(array[0])):
        array[i][j+(m-1-2*j)*(i%2)]