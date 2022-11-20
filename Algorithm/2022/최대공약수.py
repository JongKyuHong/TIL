import sys
input = sys.stdin.readline

def gcd(n,m):
	while m>0:
		n,m = m, n%m
	return n

n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))
n_num = 1
m_num = 1
for i in n_list:
	n_num *= i
for i in m_list:
	m_num *= i

print(str(gcd(n_num,m_num))[-9:])