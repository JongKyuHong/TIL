n ,c = map(int,input().split())  # n 마을수, c 트럭의 용량
m = int(input())  # m 박스정보의 개수
array = []
for _ in range(m):
    array.append(list(map(int,input().split())))
array.sort()
print(array)

