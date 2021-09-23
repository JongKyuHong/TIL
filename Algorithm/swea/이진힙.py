def insert_heap(i):
    heap.append(i)
    index = len(heap)-1
    while index > 1 and heap[index] < heap[index//2]:
        heap[index], heap[index//2] = heap[index//2], heap[index]
        index //= 2


def get_sum(index):
    ans = 0
    while index != 0:
        index //= 2
        ans += heap[index]
    return ans



for test_case in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    heap = [0]
    for i in array:
        insert_heap(i)
    ans = get_sum(len(heap)-1)
    print(f'#{test_case} {ans}')