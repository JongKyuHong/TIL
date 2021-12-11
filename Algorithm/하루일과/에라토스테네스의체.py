# 다수의 자연수에 대하여 소수를 판별할때 사용
# 1. 2부터 N까지의 모든 자연수를 나열한다.
# 2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
# 3. 남은 수 중에서 i의 배수를 모두 제거한다(i는 제거하지 않는다.)
# 4. 더 이상 반복할 수 없을때 까지 2번과 3번의 과정을 반복한다.

import math

n = 1000 # 2부터 1000까지
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')            