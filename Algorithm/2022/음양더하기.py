def solution(absolutes, signs):
    ans = 0
    print(signs)
    for a, s in zip(absolutes, signs):
        if s:
            ans += a
        else:
            ans -= a
    return ans
