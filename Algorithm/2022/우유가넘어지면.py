d={'.':'.','O':'O','-':'|','|':'-','\\':'/','/':'\\','^':'<','<':'v','v':'>','>':'^'}

n,m=map(int,input().split(" "))
xx=[['a' for i in range(n)] for j in range(m)]
for i in range(n):
	line=input()
	for j in range(m):
		xx[m-j-1][i]=d[line[j]]
for i in range(m):
	for j in range(n):
		print(xx[i][j],end="")
	print()
