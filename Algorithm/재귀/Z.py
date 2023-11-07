import sys 
input = sys.stdin.readline

def solve(n, x, y):
	global cnt
	if x > r or x+n <= r or y > c or y+n <= c:
		cnt += n**2
		return
	if n > 2:
		n//=2
		solve(n, x, y)
		solve(n, x, y+n)
		solve(n, x+n, y)
		solve(n, x+n, y+n)
	else:
		if x == r and y == c:
			print(cnt)
			return
		if x == r and y+1 == c:
			print(cnt+1)
			return
		if x+1 == r and y == c:
			print(cnt+2)
			return
		if x+1 == r and y+1 == c:
			print(cnt+3)
			return

N, r, c = map(int, input().split())
cnt = 0
solve(2**N, 0, 0)