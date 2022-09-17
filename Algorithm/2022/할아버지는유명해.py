while 1:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    score = {}
    for _ in range(n):
        input_data = list(map(int, input().split()))
        for i in input_data:
            if i in score:
                score[i] += 1
            else:
                score[i] = 1
    s = sorted(score.items(), key=lambda x:-x[1])
    max_s = s[0][1]
    standard = 0
    res = []
    for i in range(1, len(s)):
        if max_s > s[i][1] and standard == 0:
            standard = s[i][1]
        if standard == s[i][1]:
            res.append(s[i][0])
    res.sort()
    print(*res)