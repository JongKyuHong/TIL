import sys
input = sys.stdin.readline

words = input().rstrip()
dic = [0 for i in range(27)]
for word in words:
    dic[ord(word)-65] += 1

oddIndex = -1
for i in range(27):
    if dic[i] % 2:
        if oddIndex != -1:
            print("I'm Sorry Hansoo")
            exit()
        else:
            oddIndex = i
res = ''
for i in range(27):
    for _ in range(dic[i]//2):
        res += chr(65+i)
res_reverse = res[::-1]
if oddIndex != -1:
    res += chr(65+oddIndex)
res += res_reverse
print(res)