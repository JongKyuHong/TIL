from collections import deque

n = int(input())
energy = list(map(int, input().split()))
energy.sort(reverse=True)
len_energy = len(energy)
sum = energy[0]
for i in range(1, n):
    sum += (energy[i]/2)

print(sum)