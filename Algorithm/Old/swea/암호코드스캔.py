# import sys
# sys.stdin = open('input.txt')

hex = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
    '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}
decryption = {'112': 0, '122': 1, '221': 2, '114': 3, '231': 4,
              '132': 5, '411': 6, '213': 7, '312': 8, '211': 9}


def Verification(nums):
    result = (int(nums[0]) + int(nums[2]) + int(nums[4]) + int(nums[6])) * 3 + int(nums[1]) + int(nums[3]) + int(nums[5]) + int(nums[7])
    if result % 10:
        return False
    else:
        return True

for test_case in range(int(input())):
    n, m = map(int, input().split())
    array = [input() for _ in range(n)]
    conversion = [[] for _ in range(len(array))]
    for i in range(len(array)):
        new_bin = ''
        for j in array[i]:
            # new_bin += format((int(j, 16)),'b')
            new_bin += hex[j]
        conversion[i] = new_bin
    ans = 0
    answer = []
    visited = []
    for i in range(n):
        c1_1 = c0_1 = c1_2 = 0
        for j in range((m*4)-1, -1, -1):
            if conversion[i][j] == '1' and c0_1 == 0 and c1_2 == 0:
                c1_1 += 1
            elif conversion[i][j] == '0' and c1_1 > 0 and c1_2 == 0:
                c0_1 += 1
            elif conversion[i][j] == '1' and c1_1 > 0 and c0_1 > 0:
                c1_2 += 1
            if conversion[i][j] == '0' and c1_1 > 0 and c0_1 > 0 and c1_2 >0:
                min_value = min(c1_1, c0_1, c1_2)
                c1_1 = c1_1//min_value
                c0_1 = c0_1 // min_value
                c1_2 = c1_2 // min_value
                res = decryption[str(c1_1)+str(c0_1)+str(c1_2)]
                answer.append(res)
                c1_1 = c0_1 = c1_2 = 0
            if len(answer) == 8:
                result = answer[::-1]
                if Verification(result) and result not in visited:
                    ans += sum(result)
                visited.append(result)
                res = []

    print(f'#{test_case + 1} {ans}')


