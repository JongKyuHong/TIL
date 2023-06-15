import sys
input = sys.stdin.readline

T = int(input())

# 2는 1, 3은 클때 기준 7, 4는 클때 11 작을때 4, 5는 클때 
#big = [1, 7, 11, 71, 111, 75, 91, 97] # 2 3 4 5 6 7 8 9

# 하면 할수록 2랑 3계속 반복 즉, 1이랑 7만 번갈아가며 나옴 자리만 바뀌어서
big = [0]*101
# 이런식으로
string = ['1']
for i in range(2, 101):
    big[i] = int(''.join(string))
    if i % 2 == 0:
        string[0] = '7'
    else:
        string[0] = '1'
        string.append('1')
#nums = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
#small = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 23, 20, 60, 90, 99, 108] # 10개가 뭐지 23 11 20 12개 13개

# 가장 합리적인 조합으로 (가장 작아야하므로 가장 획수가 많은것을 사용해야 한다.)
#small = {0 : 0, 1: 0, 2: 1, 3: 7, 4: 4, 5: 2, 6: 6, 7:8, 8:10, 9: 18, 10:23}

# 8부터 6+2 로 들어감 그게 젤 작음 이때부터는
small = [0] *101
small[2] = 1
small[3] = 7
small[4] = 4
small[5] = 2
small[6] = 6
small[7] = 8
small[8] = 10
# 9부터는 아래것들 더해서 구함 2+7 3+6 4+5 이런식으로?
# 10은 22
# 나를 만드는데 필요한 획수
# 2, 3, 4, 5, 6, 7, 8
for i in range(9, 101):
    small[i] = min( 
        int(str(small[i-2])+'1'), int('1'+str(small[i-2])), 
        int(str(small[i-3])+'7'), int('7'+str(small[i-3])),
        int(str(small[i-4])+'4'), int('4'+str(small[i-4])),
        int(str(small[i-5])+'2'), int('2'+str(small[i-5])),
        int(str(small[i-6])+'6'), int('6'+str(small[i-6])), int(str(small[i-6])+'0'),
        int(str(small[i-7])+'8'), int('8'+str(small[i-7]))
    )
for _ in range(T):
    n = int(input())
    print(small[n], big[n])
