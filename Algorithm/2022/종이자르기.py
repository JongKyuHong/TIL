def solution(M, N):
    answer = 0
    if M == 1 and N == 1:
        return 0
    answer = M-1
    cnt = M*(N-1)
    print(answer, cnt)
    return answer+cnt

print(solution(2,2))
print(solution(2,5))
print(solution(3,5))