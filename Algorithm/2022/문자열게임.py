import sys
input = sys.stdin.readline

for _ in range(int(input())):
    w = input()
    k = int(input())
    word = {}
    short_v, long_v = 0, 0
    idx, flag = 0, 0
    for i in range(len(w)):
        if w[i] in word:
            word[w[i]] += 1
            if word[w[i]] == k and flag == 0:
                short_v = i
                flag += 1
        else:
            word[w[i]] = 1

        


