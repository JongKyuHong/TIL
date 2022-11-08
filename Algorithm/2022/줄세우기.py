import sys
input = sys.stdin.readline

n = int(input())
lst = []
lst2 = []
lst3 = []
for _ in range(n):
    input_data = input().rstrip()
    lst.append(input_data)
    lst2.append(input_data)
    lst3.append(input_data)

lst.sort()
lst2.sort(reverse=True)
if lst == lst3:
    print('INCREASING')
elif lst2 == lst3:
    print('DECREASING')
elif lst3 != lst and lst3 != lst2:
    print('NEITHER')