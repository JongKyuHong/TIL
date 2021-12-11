## 1. 행 우선 순회
# i 행의좌표, j 열의좌표
for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j]

## 2. 열 우선 순회
for i in range(len(array[0])):
    for j in range(len(array)):
        array[j][i]

## 3. 지그재그순회
for i in range(len(array)):
    for j in range(len(array[0])):
        array[i][j+(m-1-2*j)*(i%2)]  # i가 홀수이면  -j 오 -> 왼, i가 짝수이면 왼 -> 오

## 4. 전치행렬
for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] =  arr[j][i], arr[i][j]