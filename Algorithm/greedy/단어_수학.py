n = int(input())
words = []
for _ in range(n):
    words.append(input().rstrip())
      
alpha_list = [0 for i in range(26)]

for word in words:
    length = len(word)
    for i in range(len(word)):
        alpha_list[ord(word[i]) - ord('A')] += pow(10,length-i-1)

result = 0
alpha_list.sort(reverse=True)
for i in range(9,0,-1):
    result += i*alpha_list[9-i]

print(result)
        


