import sys
input = sys.stdin.readline

n = int(input())


target = input().rstrip()
len_target = len(target)
words = []
res = 0
for _ in range(n):
    words.append(input().rstrip())

for word in words:
    idx = 0
    target_idx = 0
    len_word = len(word)
    flag = 0
    while idx < len_word:
        if word[idx] == target[0]:
            gap = 1
            while (len_word-idx)/gap > len_target-1:
                #print(gap, word,idx,'gapword')
                target_idx = 0
                for i in range(idx, len(word), gap):
                    if word[i] == target[target_idx]:
                        target_idx += 1
                        if target_idx == len_target:
                            res += 1
                            #print(word,'wr')
                            flag = 1
                            break
                    else:
                        break
                if flag:
                    break
                else:
                    gap += 1
        if flag:
            break
        idx += 1
print(res)