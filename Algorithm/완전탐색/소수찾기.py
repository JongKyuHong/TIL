from itertools import permutations

def check(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    lista = []
    for i in numbers:
        lista.append(i)
    a = list(map(''.join,permutations(lista,len(lista))))
    print(a)
    for i in a:
        if check(int(i)):
            answer.append(i)
    for i in numbers:
        if i == '0':
            continue
        elif check(int(i)):
            answer.append(i)
    return len(set(answer))

print(solution("17"))




