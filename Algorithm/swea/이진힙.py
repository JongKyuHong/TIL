def insert_heap(data):
    heap.append(data)
    index = len(heap) - 1
    while index > 1 and heap[index] < heap[index//2]:
        heap[index], heap[index//2] = heap[index//2], heap[index]
        index //= 2


def get_sum_heap():
    value = 0
    idx = N//2
    while idx:
        value += heap[idx]
        idx //= 2
    return value



for test_case in range(int(input())):
    ans = 0
    N = int(input())
    user_input = list(map(int, input().split()))
    heap = [0]
    for data in user_input:
        insert_heap(data)
    ans = get_sum_heap()

    print(f'#{test_case+1} {ans}')
