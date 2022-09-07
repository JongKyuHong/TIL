import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
blue, white = 0, 0

def check(r1, c1, r2, c2):
    idx = 0
    standard = -1
    for i in range(r1, r2):
        for j in range(c1, c2):
            if idx == 0:
                standard = graph[i][j] 
            else:
                if standard != graph[i][j]:    
                    return -1
            idx += 1
    return standard

def find(r1, c1, r2, c2):
    global blue, white
    if r2-r1 == 1 and c2-c1 == 1:
        if graph[r1][c1] == 1:
            blue += 1
        else:
            white += 1
        return
    standard = check(r1, c1, r2, c2)
    if standard != -1:
        if standard == 1:
            blue += 1
        elif standard == 0:
            white += 1
        return
    else:
        print(r1, c1, r2//2, c2//2, 'aaa1')
        print(r1, c1+c2//2, r2//2, c2, 'aaa2')
        print(r1+r2//2, c1, r2, c2//2, 'aaa3')
        print(r1+r2//2, c1+c2//2, r2, c2, 'aaa4')
        exit()
        find(r1, c1, r2//2, c2//2)
        find(r1, c1+c2//2, r2//2, c2)
        find(r1+r2//2, c1, r2, c2//2)
        find(r1+r2//2, c1+c2//2, r2, c2)

        

find(0, 4, 4, 8)
print(white)
print(blue)