from collections import deque

n,m = map(int,input().split())

books = list(map(int,input().split()))
books.sort()
book_g1 = [] # 음
book_g2 = [] # 양
for i in range(n):
    if books[i] < 0:
        book_g1.append(books[i])
    else:
        book_g2.append(books[i])
book_g2.sort(reverse=True)
book_g1.sort()
g1 = deque(book_g1)
g2 = deque(book_g2)
sum = 0
index = 0
if book_g1 and book_g2:
    if abs(min(book_g1)) > max(book_g2): # g1의 최댓값이 더 크면 g2부터 순회를 한다.
        target = g1[0]
        while len(g2)>m:
            for i in range(m):
                g2_v = g2.popleft()
                if index == 0:
                    sum += 2*g2_v
                    index = 1
            index = 0
        if g2:
            g2_v = g2.popleft()
            sum += 2*g2_v
            #print(sum)
        while len(g1) > m:
            for i in range(m):
                g1_v = g1.popleft()
                if index == 0:
                    sum -= 2*g1_v
                    #print(sum)
                    index = 1
            index = 0
        if g1:
            g1_v = g1.popleft()
            sum -= 2*g1_v
            #print(sum)
        print(sum+target)
    else:
        target = g2[0]
        while len(g1)>m:
            for i in range(m):
                g1_v = g1.popleft()
                if index == 0:
                    sum -= 2*g1_v
                    index = 1
            index = 0
        if g1:
            g1_v = g1.popleft()
            sum -= 2*g1_v
        while len(g2) >m:
            for i in range(m):
                g2_v = g2.popleft()
                if index == 0:
                    sum += 2*g2_v
                    index = 1
            index = 0
        if g2:
            g2_v = g2.popleft()
            sum += 2*g2_v
        print(sum-target)
elif book_g1:
    target = g1[0]
    while len(g1) > m:
        for i in range(m):
            g1_v  = g1.popleft()
            if index == 0:
                sum -= 2*g1_v
                index = 1
        index = 0
    if g1:
        g1_v = g1.popleft()
        sum -= 2*g1_v
    print(sum+target)
else:
    target = g2[0]
    while len(g2) > m:
        for i in range(m):
            g2_v  = g2.popleft()
            if index == 0:
                sum += 2*g2_v
                index = 1
        index = 0
    if g2:
        g2_v = g2.popleft()
        sum += 2*g2_v
    print(sum-target)