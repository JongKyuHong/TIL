for _ in range(4):
    a1, a2, b1, b2, a3, a4, b3, b4 = map(int, input().split())
    result = 'a'
    if a2 == b4 or b1 == a3 or b2 == a4 or b3 == a1:
        result = 'b'
    elif [a1,a2] == [a3,a4] or [a1,a2] == [b3,b4] or [b1,b2] == [a3,a4] or [b1,b2] == [b3,b4]:
        result = 'c'
    elif b2 < a4 or b4 < a2 or a1 > b3 or b1 < a3:
        result = 'd'
    print(result)