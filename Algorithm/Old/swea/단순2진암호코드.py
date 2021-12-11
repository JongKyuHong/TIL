decryption = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
         '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

def data_extraction(arr):
    global n, m, data
    for y in range(n):
        for x in range(m-1, -1, -1):
            if array[y][x] == '1':
                data = array[y][x-55:x+1]
                return data


for test_case in range(int(input())):
    n, m = map(int, input().split()) # 세로크기n, 가로크기m
    array = [input() for _ in range(n)]
    data = ''
    data_extraction(array)
    result = []
    start_i = 0
    end_i = 6

    for _ in range(8):
        result.append(decryption[data[start_i:end_i+1]])
        start_i += 7
        end_i += 7
    value = (result[0] + result[2] + result[4] + result[6])*3 + (result[1]+result[3]+result[5]) + result[7]
    if not value % 10:
        print(f'#{test_case+1} {sum(result)}')
    else:
        print(f'#{test_case+1} 0')