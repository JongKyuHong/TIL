n = int(input())
array = []
for _ in range(n):
    d,w,d1,w1 = list(map(int,input().split()))
    array.append([(d,w),(d1,w1)])
array.sort(key=lambda x:(x[0],x[1]))
i = -1
end = (3,1)
result = []
flag = 0
temp = (0,0)
while end <= (11,30) and i<n: # 모든 리스트를 다봤을때 , end값이 11월30일을 넘었을때 종료
    flag = 0
    i+=1
    for j in range(i,n): 
        if array[j][0] > end: # 엔드값보다 꽃심는날이 더 뒤일경우
            break
        if temp < array[j][1]:
            temp = array[j][1]
            print(temp,j)
            i = j
            flag = 1
    if flag == 1:  # 변했을때
        print(temp)
        end = temp 
        result.append(array[i])  #결과 리스트에 아무값이나 추가(결과가 바뀌었다는 소리)
    else:
        result = []
        break

print(len(result))
# import sys
# accumulation={1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334} 
# def md_to_d(month, day): 
#     return accumulation[month]+day

# flowers=[] 
# N=int(sys.stdin.readline()) 
# for i in range(N): 
#     start_month, start_day, end_month, end_day=map(int, sys.stdin.readline().split()) 
#     flowers.append((md_to_d(start_month, start_day), md_to_d(end_month, end_day))) 
# print(flowers)
# selected=[] 
# start=0 
# end=60 
# startdate=60 
# enddate=334 
# flowers.sort(key=lambda x:(x[0], x[1])) 
# x=-1 
# temp=0 
# changed=0 
# selected=[] 
# while end<=enddate and x<N: 
#     changed=0 
#     x+=1 
#     for i in range(x, N): 
#         if flowers[i][0]>end: 
#             break 
#         if temp<flowers[i][1]: 
#             temp=flowers[i][1] 
#             print(temp,x)
#             x=i 
#             changed=1 
#     if changed==1: 
#         end=temp 
#         print(end)
#         selected.append(flowers[x]) 
#     else: 
#         selected=[] 
#         break
# print(len(selected))

