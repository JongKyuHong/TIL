import sys
input = sys.stdin.readline

for _ in range(int(input())):
    input_ = input().rstrip()
    idx = 0
    answer = []
    for inp in input_:
        if inp == '>':
            idx += 1
        elif inp == '<':
            idx -= 1
        elif inp == '-':
            if idx > 0 and answer:
                if idx > len(answer):
                    idx = len(answer)
                answer.pop(idx-1)
                idx -= 1
        else:
            if idx < 0:
                idx = 0
            elif idx > len(answer):
                idx = len(answer)
            answer.insert(idx, inp)
            idx += 1
    print(''.join(answer))
#https://www.acmicpc.net/problem/5397 다시