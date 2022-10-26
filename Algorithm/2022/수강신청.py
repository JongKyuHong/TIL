import sys
input = sys.stdin.readline

k, l = map(int, input().split())
stack = {}
for idx in range(l):
    nums = input().rstrip()
    stack[nums] = idx

# target = sorted(stack.items(), key=lambda x:x[1])
# for k, v in target[:k]:
#     print(k)
for key, value in sorted(stack.items(), key=lambda x:x[1])[:k]:
    print(key)