list_a = ['C','A','M','B','R','I','D','G','E']
n = input()
res = ''
for i in n:
    if i not in list_a:
        res += i
print(res)

