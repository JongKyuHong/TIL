t = int(input())

def selectionSort(a):
    for i in range(0,len(a)-1):
        min = i
        for j in range(i+1,len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min],a[i]

for test_case in range(1,t+1):
    n = int(input())
    array = list(map(int,input().split()))
    selectionSort(array)
    print(f'#{test_case}', *array)





