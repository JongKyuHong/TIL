s = input()

s = list(s)
answer = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        s[i+1] = str(1 - int(s[i+1]))
        j = i
        while j < len(s)-2:
            j += 1
            if s[j] != s[j+1]:
                s[j+1] = str(1-int(s[j+1]))
            elif s[j] == s[j+1]:
                break
        answer += 1
print(answer)

