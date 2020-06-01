def find_pairs(arr1,arr2,target):
    pairs = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] + arr2[j] in list(range(target-1,target+2)):
                pairs.append(arr1[i])
                pairs.append(arr2[j])
    print(pairs)


find_pairs([13,5,7,12,0], [4,9,23,5,1], 19)