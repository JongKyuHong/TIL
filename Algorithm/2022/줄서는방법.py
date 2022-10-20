import math

def solution(n, k):
    answer = [x for x in range(1, n+1)]
    stack = []
    k -= 1
    
    while answer:
        print(math.factorial(n-1), 'asdf')
        a = k // math.factorial(n-1)
        print(a,'asdf2')
        stack.append(answer[a])
        del answer[a]

        k = k % math.factorial(n-1)
        n -= 1
    
    return stack
print(solution(3, 5))