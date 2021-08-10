t = int(input())

for test_case in range(1,t+1):
    n_input = list(input())
    m_input = list(input())
    array = []
    maxa = 0
    for i in set(n_input):
        maxa = max(maxa,m_input.count(i))
    print(f'#{test_case} {maxa}')



