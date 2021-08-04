from abc import abstractproperty


n,k = map(int,input().split()) # n식탁의 길이 k 햄버거를 선택할수있는 거리
array = input() # h 햄버거 p 사람
list_s = list(array)
cnt = 0

for i in range(n):
    if array[i] == 'P':
        for j in range(i-k,i+k+1):
            if 0 <=j < n and list_s[j] == 'H':
                cnt += 1
                list_s[j] ='-'
                break
print(cnt)