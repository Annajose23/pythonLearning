from collections import Counter

def commonChild(s1,s2):
    res = []
    res_arr = {}
    for item in s1:
        if item in res_arr:
            res_arr[item] += 1
        else:
            res_arr[item] = 1
    print(res_arr)
    for item in s2:
        if item in res_arr and res_arr[item] >= 1:
            res_arr[item] -= 1
            res.append(item) 
    print(res)
    return len(res)
        


    
print(commonChild("SHINCHAN", "NOHARAAA"))