import sys
input = sys.stdin.readline

p = int(input())
for _ in range(p):
    dic = {'TTT':0, 'TTH':0, 'THT':0, 'THH':0, 'HTT':0, 'HTH':0,'HHT':0,'HHH':0}
    input_data = input().rstrip()
    test = input_data[:2]
    for i in range(2,40):
        test += input_data[i]
        dic[test] += 1
        test = test[1:]
    for v in dic.values():
        print(v, end=' ')
