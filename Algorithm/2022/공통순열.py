from collections import defaultdict

while True:
    try:
        a=input()
        b=input()
        # alpha1=defaultdict(int)
        # alpha2=defaultdict(int)
        alpha1 = {}
        alpha2 = {}
        ans=''
        for s in a:
            if s not in alpha1:
                alpha1[s] = 1
            else:
                alpha1[s]+=1
        for s in b:
            if s not in alpha2:
                alpha2[s] = 1
            else:
                alpha2[s]+=1
        s = []
        for char in alpha1:
            print(char, 'char')
            if char in alpha2:
                s.append(char)
        s.sort()
        for char in s:
            ans += char*min(alpha1[char],alpha2[char])
        print(ans)
    except:
        break