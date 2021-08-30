w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
x_list = list(range(w)) + list(range(w,0,-1))
y_list = list(range(h)) + list(range(h,0,-1))

result_x = x_list[(p+t)%(2*w)]
result_y = y_list[(q+t)%(2*h)]

print(result_x, result_y)