n = int(input())

top = []
max_height = 0
max_index = 0
start_index = 1000
end_index = 1
for _ in range(n):
    index, height = map(int,input().split())
    if height > max_height:
        max_height = height
        max_index = index
    if start_index > index:
        start_index = index
    if end_index < index:
        end_index = index
    top.append([index,height])

m_list = [0] * (end_index+1)
for l, h in top:
    m_list[l] = h
prev = 0
res = 0
for i in range(max_index+1):
    if m_list[i] > prev:
        prev = m_list[i]
    res += prev

prev = 0
for i in range(end_index,max_index,-1):
    if m_list[i] > prev:
        prev = m_list[i]
    res += prev

print(res)