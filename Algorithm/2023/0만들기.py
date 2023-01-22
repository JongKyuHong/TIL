import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    ans = []
    def dfs(lst, num, string):
        if num == N:
            lst.reverse()
            while len(lst) > 1:
                if lst[-1] not in ['+','-']:
                    num1 = lst.pop()
                    op = lst.pop()
                    num2 = lst.pop()
                    if op == '+':
                        lst.append(num1+num2)
                    else:
                        lst.append(num1-num2)
            num1 = lst.pop()
            if num1 == 0:
                ans.append(string)
            return
        for i in range(3):
            if i == 0:
                dfs(lst+['+']+[num+1], num+1, string+'+'+str(num+1))
            elif i == 1:
                dfs(lst+['-']+[num+1], num+1, string+'-'+str(num+1))
            else:
                dfs(lst+[int(str(lst.pop())+str(num+1))], num+1, string+' '+str(num+1))
    dfs([1], 1, '1')
    for i in sorted(ans):
        print(i)
    print()