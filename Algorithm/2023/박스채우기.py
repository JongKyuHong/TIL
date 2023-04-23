import sys
input = sys.stdin.readline

length, width, height = map(int, input().split())
N = int(input())
cube = []
for _ in range(N):
    A, B = map(int, input().split())
    cube.append(B)


