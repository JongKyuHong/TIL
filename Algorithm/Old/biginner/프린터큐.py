from collections import deque

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())  # n은 문서의 갯수, m은 몇번째로 인쇄되었는지 궁금한 문서가 현재 몇번째인지
    array = list(map(int,input().split()))
    que = deque(array)
    idx, cnt = m, 0
    while que:
        maxq = max(que)
        quepop = que.popleft()
        if not que:
            cnt += 1
            break
        if maxq > quepop:
            que.append(quepop)
            if idx == 0:
                idx = len(que)
        else:
            cnt += 1
            if idx == 0:
                break
        idx -= 1
    print(cnt)


