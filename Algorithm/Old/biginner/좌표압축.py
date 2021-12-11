import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

arr2 = sorted(list(set(arr)))  # set을 통해 중복을 제거, 오름차순정렬
dic = {arr2[i]: i for i in range(len(arr2))}  # 딕셔너리로 인덱스를 입력해 저장
print(dic)
for i in arr:
    print(dic[i],end=' ')