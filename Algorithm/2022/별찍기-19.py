n = int(input())

stars = [[' ' for _ in range(4*n-3)] for _ in range(4*n-3)]

def fill_star(n,r,c):
    if n == 1:
        stars[r][c] = '*'
        return
    
    length = 4*n-3

    for i in range(length):
        stars[r][c+i] = '*'
        stars[r+i][c] = '*'
        stars[r+length-1][c+i] = '*'
        stars[r+i][c+length-1] = '*'
    
    fill_star(n-1,c+2,r+2)

fill_star(n, 0, 0)
for s in stars:
    print(''.join(s))