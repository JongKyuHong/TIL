import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
for _ in range(n):
    site, password = input().rstrip().split()
    dic[site] = password

for _ in range(m):
    input_data = input().rstrip()
    print(dic[input_data])