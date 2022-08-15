from tkinter.filedialog import FileDialog


n, m = map(int, input().split()) # main 폴더 하위에 있는 폴더의 총 개수, 파일의 총개수

Folder_dict = {}
File_dict = {}
File_dict_v = {}
#파일의 종류의 갯수와 총 갯수를 알아야한다.
for _ in range(n+m):
    P, F, C = input().split() # 상위 폴더의 이름, 폴더나 파일이름, 폴더인지 아닌지 알려주는 값
    
    if C == '1': # 폴더가 주어질 경우
        if P in Folder_dict: # 하위 파일의 종류의 갯수 파악
            Folder_dict[P] += [F]
        else:
            Folder_dict[P] = [F]
    elif C == '0':
        if P in File_dict: 
            File_dict[P] += 1 # 하위 파일의 총 갯수 파악
            File_dict_v[P] += [F] # 하위 파일의 종류 파악
        else:
            File_dict[P] = 1
            File_dict_v[P] = [F]

Q = int(input())
path = []
for _ in range(Q):
    data = input().split('/')
    path.append(data[-1])
    
def find(v):
    global cnt, cnt2
    if v in Folder_dict:
        for i in Folder_dict[v]:
            find(i)
    if v in File_dict:
        cnt += File_dict[v]
    if v in File_dict_v:
        for i in File_dict_v[v]:
            res.add(i)

for p in path:
    cnt,cnt2 = 0,0
    res = set()
    find(p)
    cnt2 = len(res)
    print(cnt2,cnt)
