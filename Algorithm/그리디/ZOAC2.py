word = list(input()) #문자열
start = 'A' 
time = 0 
for i in word: 
    left = ord(i) - ord(start) #원판 왼쪽으로 돌리기 
    right = ord(start) - ord(i) 
    if left < 0: 
        left += 26 
    elif right < 0: 
        right += 26 
    time += min(left, right) 
    start = i 

print(time)

