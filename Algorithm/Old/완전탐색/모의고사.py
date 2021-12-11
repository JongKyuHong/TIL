def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    result = []

    for idx, answer in answers:
        if answer == s1[idx%len(s1)]:
            score[0] += 1
        if answer == s2[idx%len(s2)]:
            score[1] += 1
        if answer == s3[idx%len(s3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    return result

