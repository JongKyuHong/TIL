import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    N_str = str(N)[::-1]
    print("YES" if str(int(N_str)+N)[::-1] == str(int(N_str)+N) else "NO")