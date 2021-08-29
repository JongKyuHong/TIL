w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

w_list = []
h_list = []

for i in range(w):
    w_list.append(i)
for j in range(w, 0, -1):
    w_list.append(i)

for i in range(h):
    h_list.append(i)
for j in range(h, 0, -1):
    h_list.append(i)

x = w_list[(p+t) % (2*w)]
y = h_list[(q+t) % (2*h)]

print(x, y)


