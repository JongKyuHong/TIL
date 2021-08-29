n, k = map(int ,input().split())
array = list(map(int, input().split()))
max_value = sum(array[0:k])
max_array = max_value
for i in range(n-k):
    max_value = max_value - array[i] + array[i+k]
    max_array = max(max_array, max_value)
print(max_array)