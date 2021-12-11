n = int(input())

def sc(text,left,right):
    while (left<right):
        if text[left] == text[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def fc(text,left,right):
    while (left < right):
        if text[left] == text[right]:
            left += 1
            right -= 1
        else:
            check1 = sc(text,left+1,right)
            check2 = sc(text,left,right-1)
            if check1 or check2:
                return 1
            else:
                return 2
    return 0
for _ in range(n):
    text = input()
    left = 0
    right = len(text) - 1
    ans = fc(text,left,right)
    print(ans)

# *2는 무조건 짝수다 ,, 즉슨 하나가 삐져나온경우는 무조건 홀수일수밖에 없다.
# 양쪽에서 다가가면서 하나씩 넣고 그게 다른경우 바로앞에 있는 원소를 서로 교차해서 확인했는데 같으면 유사회문 아니면 2