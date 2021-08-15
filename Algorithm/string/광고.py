import sys
 
def failure(pattern): # aaaaa
    table = [0] * len(pattern) # 00000
    j = 0
    for i in range(1, len(pattern)): # 1부터 5까지 ,, 2번째
        # j가 0보다 크고 패턴i번째가 (즉 넘겨온아이가 j번째 요소와 다르면) , i는 1이고 j는 1이다 
        # i를 0으로 봤을때 pattern[1] != pattern[0]이면 pattern[1] == a , pattern[0] == a
        while j > 0 and pattern[i] != pattern[j]: # i가 1 이고 j가 1이기 때문에 pattern 1은 둘다 같은 것이다.
            j = table[j-1]  # j에 table의 j-1번쨰 요소를 넣는다  # j에 table[0]의 값을 넣는다?
        if pattern[i] == pattern[j]:  # pattern[0] == a , pattern[1] == a  , 
            j += 1  # j를 높임
            table[i] = j  # table의 1번째 요소(0)에 1을 넣는다. j값은 1 이겠죠?
    print(table)
    return table

n = int(sys.stdin.readline())
pat = sys.stdin.readline().rstrip() # aaaaa
print(n - failure(pat)[n-1]) # aaaaa (5- failure(aaaaa)[4])


