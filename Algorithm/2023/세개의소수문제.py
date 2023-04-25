def find(num):
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                if primes[i] + primes[j] + primes[k] == num:
                    return [primes[i], primes[j], primes[k]]

nums = [0, 0] + [1]*(999)
primes = []

for i in range(2, 1001):
    if nums[i]:
        primes.append(i)
        for j in range(2*i, 1001, i):
            nums[j] = 0

for _ in range(int(input())):
    K = int(input())
    print(*find(K))
