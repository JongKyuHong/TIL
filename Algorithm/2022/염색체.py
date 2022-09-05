import sys
input = sys.stdin.readline

for _ in range(int(input())):
    alphabets = input()
    a = alphabets.find("A")
    f = alphabets.find("F")
    c = alphabets.find("C")
    flag = False
    if a < 0 or f < 0 or c < 0 or a > f or a > c or f > c:
        flag = True

    if flag or alphabets[0] not in ["A", "B", "C", "D", "E", "F"]:
        flag = True
    
    if not flag:
        for i in range(a, f):
            if alphabets[i] != "A":
                flag = True
                break
    
    if not flag:
        for j in range(f, c):
            if alphabets[j] != "F":
                flag = True
                break
    
    c_end = 0
    if not flag:
        for k in range(c, len(alphabets)):
            if alphabets[k] != "C":
                break
            else:
                c_end = k
    
    if len(alphabets) - c_end > 1:
        flag = True
    
    if alphabets[-1] not in ["A", "B", "C", "D", "E", "F"]:
        flag = True
    
    