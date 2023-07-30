def solution(m, n, startX, startY, balls):
    answer = []
    for ball_x, ball_y in balls:
        tmp = float('inf')
        if not (ball_x == startX and startY < ball_y): # 위쪽벽으로 쿠션하는 경우
            tmp = min(tmp, (startX-ball_x)**2 + (startY-n+ball_y-n)**2)
        if not (ball_x == startX and startY > ball_y): # 아래쪽으로 쿠션하는 경우
            tmp = min(tmp, (startX-ball_x)**2 + (startY+ball_y)**2)
        if not (ball_y == startY and startX > ball_x): # 왼쪽으로 쿠션하는 경우
            tmp = min(tmp, (startY-ball_y)**2 + (startX+ball_x)**2)
        if not (ball_y == startY and startX < ball_x): # 오른쪽 쿠션
            tmp = min(tmp, (startY-ball_y)**2 + (startX-m+ball_x-m)**2)
        answer.append(tmp)
    return answer