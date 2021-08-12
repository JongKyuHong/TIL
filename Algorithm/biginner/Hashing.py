def hash1(a):
    return int(ord(a) - 96)

l = int(input())
text = input()
cnt = 0
for i in range(l):
    cnt += (31**i)*hash1(text[i])
print(cnt%1234567891)




