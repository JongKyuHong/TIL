import sys 
input = sys.stdin.readline

def dfs(idx, nums, op, flag):
    global answer, len_num
    if len(nums) == 1:
        answer = max(answer, nums.pop())
        return
    elif idx >= len(nums)-1:# 이미 한바퀴 다돌았으면
        while 1:
            if len(nums) == 1:
                answer = max(answer, nums.pop())
                break
            if '*' in op:
                i = op.index('*')
                a, b = nums.pop(i), nums.pop(i)
                c = op.pop(i)
                nums.insert(i, (a*b))
            else:
                a, b, = nums.pop(0), nums.pop(0)
                c = op.pop(0)
                if c == '+':
                    nums.insert(0, (a+b))
                elif c == '-':
                    nums.insert(0, (a-b))
        return
    
    if flag == 0:
        nums2 = nums[:]
        op2 = op[:]
        #print(idx, nums, op)
        a, b = nums.pop(idx), nums.pop(idx)
        c = op.pop(idx)
        if c == '+':
            nums.insert(idx, (a+b))
        elif c == '-':
            nums.insert(idx, (a-b))
        else:
            nums.insert(idx, (a*b))
        dfs(idx, nums, op, 1) # 지금하기
        dfs(idx+1, nums2, op2, 0) # 이따 계산하기
    else: # 계산을 이전에 했다.
        dfs(idx+1, nums, op, 0)

N = int(input())
lst = input().rstrip()

nums = []
op = []

for i in range(N):
    if lst[i].isdigit():
        nums.append(int(lst[i]))
    else:
        op.append(lst[i])

len_num = len(nums)
# 이번거를 지금 계산 하는지 안하는지?
answer = -float('inf')
cnt = 0
dfs(0, nums, op, 0)

print(answer)