import sys
input = sys.stdin.readline

N = int(input())

# N을 통해서 몇번째 S에 들어있는지를 파악하고 그 S를 만들어본다??
S = [3]
len_ = 3
index = 1
# m의 위치를 기록
while len_ < N:
    target = S[-1]*2 + index+3
    S.append(target)
    index += 1
    len_ = target

res = []
def find(lst,string_len,idx):
    global index, res
    if idx == index:
        res = lst[:]
        return
    lst2 = []
    for i in lst:
        lst2.append(i+string_len+idx+3)
    find(lst+[string_len]+lst2, string_len*2+idx+3,idx+1)

find([0],3,1)
print(res)
lst = []
for i in range(len(res)-1):
    lst.append(res[i+1]-res[i])
print(lst)