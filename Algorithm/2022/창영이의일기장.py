import sys
input = sys.stdin.readline

word = input().rstrip()
op = ['a','e','i','o','u']

answer = ''
len_word = len(word)
idx = 0
while idx < len_word:
    if word[idx] not in op:
        answer += word[idx]
        idx += 1
    else:
        answer += word[idx+2]
        idx += 3

print(answer)