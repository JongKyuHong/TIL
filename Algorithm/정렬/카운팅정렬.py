# O(n+k) 
def counting_sort(a,b,k):
    
    for i in range(0,len(b)):
        c[a[i]] += 1
    for i in range(1,len(c)):
        c[i] += c[i-1]
    
    for i in range(len(b)-1,-1,-1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -= 1



a = list(input().split())  # 입력배열
k = int(input())  # 입력의 최대값
b = []
c = [0] * (k+1)  # 카운트배열
    