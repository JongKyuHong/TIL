import sys
input = sys.stdin.readline

while 1:
    try:
        data = list(input().rstrip().split())
        res = []
        dip_idx = []
        for i in range(len(data)):
            if data[i] == 'dip':
                dip_idx.append(i)
        
        hip_i = 0
        for i in dip_idx:
            try:
                flag = 0
                for j in range(i):
                    if data[j] == 'twirl':
                        flag = 1
                        break
                
                try:
                    if data[i-1] == 'jiggle' or data[i-2] == 'jiggle':
                        continue
                    else:
                        try:
                            if i+1 < len(data)-1 and data[i+1] == 'twirl':
                                continue
                            else:
                                hip_i = i
                                res.append(1)
                                break
                        except:
                            hip_i = i
                            res.append(1)
                            break
                except:
                    try:
                        if i+1 < len(data)-1 and data[i+1] == 'twirl':
                            continue
                        else:
                            hip_i = i
                            res.append(1)
                            break
                    except:
                        hip_i = i
                        res.append(1)
                        break
            except:
                continue
        
        try:
            if not (data[-3] == 'clap' and data[-2] == 'stomp' and data[-1] == 'clap'):
                res.append(2)
        except:
            res.append(2)

        if 'twirl' in data:
            if 'hop' not in data:
                res.append(3)

        
        if data[0] == 'jiggle':
            res.append(4)
        
        if 'dip' not in data:
            res.append(5)
        
        
        if res:
            point = len(res)
            if point > 1:
                ans = ''
                if 1 in res:
                    for i in range(len(data)):
                        if i == hip_i:
                            ans += data[i].upper()
                        else:
                            ans += data[i]
                        ans += ' '
                else:
                    for i in range(len(data)):
                        ans += data[i]
                        ans += ' '
                ans2 = ''
                for i in range(point):
                    if i == point-1:
                        ans2 = ans2[:-2] + ' and ' + str(res[i])
                    else:
                        ans2 += str(res[i]) +', '
                print(f'form errors {ans2}: {ans[:-1]}')
            else:
                ans = ''
                if 1 in res:
                    for i in range(len(data)):
                        if i == hip_i:
                            ans += data[i].upper()
                        else:
                            ans += data[i]
                        ans += ' '
                else:
                    for i in range(len(data)):
                        ans += data[i]
                        ans += ' '
                print(f'form error {res[0]}: {ans[:-1]}')
        else:
            ans = ''
            for i in range(len(data)):
                ans += data[i]
                ans += ' '
            print(f'form ok: {ans[:-1]}')
    except:
        break
