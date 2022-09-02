words = []
for i in range(int(input())):
    word = input()
    words.append(word)

for word in words:
    if word[::-1] in words:
        print(len(word), word[len(word)//2])
        exit()