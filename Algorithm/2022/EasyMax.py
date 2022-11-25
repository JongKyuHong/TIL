import sys
input = sys.stdin.readline

n, q = map(int, input().split()) # 노래길이, 박자 변화량합
lst = list(map(int, input().split())) # 노래박자 빠르기
for _ in range(q):
    i, j = map(int, input().split())
    if j-1 < i:
        print(0)
    else:
        answer = 0
        for i in range(i, j):
            answer += abs(lst[i]-lst[i-1])
        print(answer)


