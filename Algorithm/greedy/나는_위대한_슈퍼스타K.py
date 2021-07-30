from operator import itemgetter

n,m,k = map(int,input().split()) # 참가자, 장르수, 본선진출자
array = []
for _ in range(m):
    array.append(list(input().split()))
new_dict = {}
count = 0
for i in array:
    if count == 0:
        for j in range(0,len(i),2):
            new_dict[i[j]] = float(i[j+1])
        count = 1
    else:
        for j in range(0,len(i),2):
            if new_dict[i[j]]:
                if new_dict[i[j]] < float(i[j+1]):
                    new_dict[i[j]] = float(i[j+1])
new_dict = sorted(new_dict.items(),key=itemgetter(1),reverse=True)
result =0
for i in new_dict:
    if k == 0:
        break
    else:
        k -= 1
        result += i[1]
print(round(result,1))
# result = 0
# for i in new_dict:
#     if k == 0:
#         break
#     else:
#         result += i
# print(result)


#array.sort(key=lambda x:x[1],reverse=True)
# for i in array:
#     #print(i) # ['2', '3.0', '1', '0.2', '3', '0.1'], ['3', '1.0', '2', '0.5', '1', '0.2']
#     for j in range(0,len(i),2):
#         print(i[j])# 2,1,3 ,,, 3 2 1

    
