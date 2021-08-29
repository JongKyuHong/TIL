k = int(input())

max_width = 0
max_height = 0
array = []
for i in range(6):
    a, b = map(int, input().split())
    if a == 1 or a == 2:
        if max_width < b:
            max_width = b
            width_index = i
    else:
        if max_height < b:
            max_height = b
            height_index = i
    array.append([a,b])

sub_w = abs(array[(width_index-1)%6][1] - array[(width_index+1)%6][1])
sub_h = abs(array[(height_index-1)%6][1] - array[(height_index+1)%6][1])

print(((max_height*max_width) - (sub_h*sub_w))*k)
