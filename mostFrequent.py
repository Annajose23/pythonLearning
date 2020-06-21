def mostFrequent(arr):
    arr_freq = {}
    for item in arr:
        if item in arr_freq:
            arr_freq[item] = arr_freq[item] + 1
        else:
            arr_freq[item] = 1
    
    arr_sorted = sorted(arr_freq.items(), key=lambda kv: kv[1], reverse=True)
    print(arr_sorted[0][0])
mostFrequent([4,1,3,3,2,1,4,1])