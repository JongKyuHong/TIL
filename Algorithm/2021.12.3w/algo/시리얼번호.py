def sum_num(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result += int(i)
    return result

n = int(input())
guitars = [input() for _ in range(n)] 
guitars.sort(key=lambda x:(len(x), sum_num(x),x))
for i in guitars:
    print(i)