import sys
input = sys.stdin.readline

sum_value = 0
sum_score = 0
for _ in range(20):
    name, score, grade = input().rstrip().split()
    score = float(score)
    if grade == 'P':
        pass
    else:
        sum_score += score
        if grade == 'A+':
            sum_value += score*4.5
        elif grade == 'A0':
            sum_value += score*4.0
        elif grade == 'B+':
            sum_value += score*3.5
        elif grade == 'B0':
            sum_value += score*3.0
        elif grade == 'C+':
            sum_value += score*2.5
        elif grade == 'C0':
            sum_value += score*2.0
        elif grade == 'D+':
            sum_value += score*1.5
        elif grade == 'D0':
            sum_value += score*1.0
print(sum_value/sum_score)



