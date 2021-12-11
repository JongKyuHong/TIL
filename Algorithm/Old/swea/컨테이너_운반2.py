def check(num):
    global val
    if num > trucks[-1]:
        return
    else:
        val += num
        trucks.pop()

for test_case in range(int(input())):
    n, m = map(int, input().split())
    con = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())))
    val = 0
    for i in con:
        if trucks:
            check(i)
        else:
            break
    print(f'#{test_case+1} {val}')
    