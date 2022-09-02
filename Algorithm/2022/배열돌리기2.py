from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
delta = ((1,0),(0,1),(-1,0),(0,-1))

def rotate(start):
    top = arr[start][start]
    left = arr[n-start-1][start]
    bottom = arr[n-start-1][m-start-1]
    right = arr[start][m-start-1]

    for i in range(start+1, m-start):
        arr[start][i-1] = arr[start][i]
    
    for i in range(n-start-1, start, -1):
        arr[i][start] = arr[i-1][start]
    
    for i in range(m-start-1, start+1, -1):
        arr[n-start-1][i] = arr[n-start-1][i-1]
    
    for i in range(start+1, n-start):
        arr[i-1][m-start-1] = arr[i][m-start-1]
    
    arr[start+1][start] = top
    arr[n-start-1][start+1] = left
    arr[n-start-2][m-start-1] = bottom
    arr[start][m-start-2] = right

size = 2*n+2*m-4

short = n if n <= m else m

for i in range(short//2):
    for _ in range(r%(size-8*i)):
        rotate(i)
