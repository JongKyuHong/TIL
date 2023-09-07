import sys 
input = sys.stdin.readline

S1, S2, S3 = map(int, input().split())
dic = {}
for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            if i + j + k not in dic:
                dic[i+j+k] = 1
            else:
                dic[i+j+k] += 1

dic = sorted(dic.items(), key=lambda x: x[0])
dic.sort(key=lambda x: x[1], reverse=True)
print(dic[0][0])

