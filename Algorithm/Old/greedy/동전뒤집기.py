# 초기상태에서 T가많은 행이나 열을 먼저 뒤집고 T가 과반이 넘는경우는 뒤집고 그렇지 않은 경우는 뒤집지 말고 그냥 두자
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input()))
def check_row(graph):
    for i in graph:
        if i.count('T') >= round(N/2):
            return False
    return True
# for i in graph:
#     if i.count('T') >= round(N//2):
#         for j in range(len(i)):
#             if i[j] == 'H':
#                 i[j] = 'T'
#             else:
#                 i[j] = 'H'
            # if j == 'H':
            #     j = 'T'
            #     print(j)
            # else:
            #     j = 'H'
            #     print(j)
# cnt = 0

# for i in range(N):
#     if list(zip(*graph))[i].count('T') >= round(N//2):
#         for j in list(zip(*graph))[i]:
#             if j == 'T':
#                 j = 'H'
#             else:
#                 j == 'T'
# for i in graph:
#     for j in i:
#         if j =='T':
#             cnt += 1
# print(cnt) 
while 1:
    if not check_row(graph):
        for i in graph:
            if i.count('T') >= round(N/2):
                for j in range(len(i)):
                    if i[j] == 'H':
                        i[j] = 'T'
                    else:
                        i[j] = 'H'
    else:
        print(graph)
        break
cnt = 0
for i in graph:
    for j in i:
        if j =='T':
            cnt += 1
print(cnt)