n,k = map(int,input().split())

array = list(map(int,input().split()))
array2 = []
count = 0
flag = 0
for i in range(len(array)):
    if array[i] in array2:
        continue
    if len(array2) < n:
        array2.append(array[i])
        continue
    multitap_idxs = []
    hasplug = True

    for j in range(n):
        if array2 in array[i:]:
            multitap_idx = array[i:].index(array2[j])
        else:
            multitap_idx = 101
            hasplug = False
        multitap_idxs.append(multitap_idx)

        if not hasplug:
            break
    plug_out = multitap_idxs.index(max(multitap_idxs))
    del array[plug_out]
    array.append(array2[i])
    count += 1
print(count)

