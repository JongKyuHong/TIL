k, n = map(int,input().split())  # 이미 가지고 있는 랜선의 갯수 k , 필요한 랜선의 갯수
array = [int(input()) for _ in range(k)]
start, end = 1, max(array)  # end값을 입력받은값중 가장 큰것으로

while start <= end: 
    mid = (start+end)//2
    cnt = 0
    for i in array:  # array에서 값을 꺼내어
        cnt += i//mid  # cnt에 추가 즉 mid로 잘랐을때 몇개가 나오는지
    if cnt >= n:  # 나온갯수가 목표보다 크거나 같은경우 스타트를 앞으로 당긴다
        start = mid + 1
    else:  # 나온갯수가 목표보다 작으면 너무 큰걸로 자른거기때문에 end를 줄인다.
        end = mid - 1
print(end)





