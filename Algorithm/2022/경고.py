data = input()
data2 = input()

hh,mm,ss=0,0,0
if data == data2:
    print("24:00:00")
    exit()
if data[:2] > data2[:2]:
    hh = 24-int(data[:2])+int(data2[:2])
elif data[:2] < data2[:2]:
    hh = int(data2[:2])-int(data[:2])

if data[3:5] > data2[3:5]:
    hh -= 1
    mm = 60-int(data[3:5])+int(data2[3:5])
elif data[3:5] < data2[3:5]:
    mm = int(data2[3:5])-int(data[3:5])

if data[6:8] > data2[6:8]:
    mm -= 1
    ss = 60-int(data[6:8])+int(data2[6:8])
elif data[6:8] < data2[6:8]:
    ss = int(data2[6:8]) - int(data[6:8])

if hh < 10:
    hh = str('0') + str(hh)
else:
    hh = str(hh)
if mm < 10:
    mm = str('0') + str(mm)
else:
    mm = str(mm)
if ss < 10:
    ss = str('0') + str(ss)
else:
    ss = str(ss)
print(f'{hh}:{mm}:{ss}')