import sys

g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(p)]
gate_clone = [0] * g
count = 0
for i in array:
    if gate_clone[i-1] == 0:
        gate_clone[i-1] = 1
        count += 1
    else:
        for j in range(i-1,-1,-1):
            if gate_clone[j] == 0:
                gate_clone[j] = 1
                count += 1
                break
        else:
            break
print(count)

