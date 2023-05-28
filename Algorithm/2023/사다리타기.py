import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
answer = list(input().rstrip())

string = []
for i in range(k):
    string.append(chr(i+65))
lst = []
target_idx = 0
for i in range(n):
    input_ = input().rstrip()
    if input_[0] == '?':
        target_idx = i
    lst.append(input_)

for j in range(target_idx):
    input_ = lst[j]
    if input_[k-2] == '-':
        string[k-2], string[k-1] = string[k-1], string[k-2]
    for i in range(k-2):
        if input_[i] == '*':
            continue
        else:
            string[i], string[i+1] = string[i+1], string[i]


for j in range(n-1, target_idx, -1):
    input_ = lst[j]
    if input_[k-2] == '-':
        answer[k-2], answer[k-1] = answer[k-1], answer[k-2]
    for i in range(k-2):
        if input_[i] == '*':
            continue
        else:
            answer[i], answer[i+1] = answer[i+1], answer[i]

ans = ''
for i in range(k-1):
    if answer[i] == string[i]:
        ans += '*'
    else:
        if i != k-2 or i != 0:
            if answer[i] == string[i+1] or answer[i] == string[i-1]:
                if ans:
                    if ans[-1] == '-':
                        ans += '*'
                    else:
                        ans += '-'
                else:
                    ans += '-'
            else:
                print('x'*(k-1))
                exit()
print(ans)