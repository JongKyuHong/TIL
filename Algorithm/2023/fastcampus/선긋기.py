import sys 
input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    numbers.append([x, y])
numbers.sort()
#print(numbers)
prev = None
answer = 0
for start, end in numbers:
    if prev == None or start >= prev:
        prev = end
        answer += abs(end-start)
    else:
        start = prev
        prev = end
        if start >= end:
            continue
        else:
            answer += abs(end-start)
print(answer)


# N은 백만개고
# 수의 범위는 20억
# 다시말해 받자마자 어떠한 처리를 해서 끝내야함
# 시간은 1초
# 대신 한번 그어진곳은 한번만 세면 된다.

# 여기가 한번이라도 그어졌는지 어떻게 판단?

# 첫번째 플랜
# 1. 시작점으로 정렬 한다. 시작점이 작을수록 앞으로 오게
# 2. 순회를 돈다. 리스트 값을 start, end 로 분해하고, end값을 저장해놓는다.
# 3. 다음 값을 만났을때 다음값의 start가 이전에 저장해놓은 end보다 크면 그냥 무시하고 end값을 저장
# 작다면 지금 start값을 이전 end값으로 바꾸고 값을 더한다. 그리고 end값 저장 
# error) 음수 값일 때 다르게 적용해야 한다.
# 지금은 start >= prev 이런식으로 사용했는데, 만약 start, prev가 둘다 음수인경우
