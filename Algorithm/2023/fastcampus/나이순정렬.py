import sys 
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    age, name = input().rstrip().split()
    lst.append([age, name])

for tmp in sorted(lst, key=lambda x: int(x[0])): # 정렬시에 문자열정렬과 숫자 정렬은 정렬방식이 좀 달라서 정수로 바꿔주지않으면 틀림
    print(*tmp)
