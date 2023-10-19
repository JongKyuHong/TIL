import sys 
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
set_lst = set(lst)
lst2 = list(set_lst)
lst2.sort()
dic = {}
for idx, value in enumerate(lst2):
    dic[value] = idx
# set으로 만든후에
# 값에 따라 정렬?
# 내 뒤에 몇개가 있는지 확인후 딕셔너리에 값하고 뒤에 몇개가 있는지로 저장

for value in lst:
    print(dic[value], end=' ')