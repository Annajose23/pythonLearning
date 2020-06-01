def twoStrings(s1, s2):
    char_frequency = {}
    s1 = s1.lower()
    s2 = s2.lower()
    for item in s1:
        if item in char_frequency:
            char_frequency[item] += 1
        else:
            char_frequency[item] = 1
    for item in s2:
        if item in char_frequency:
            result = "YES"
            break
    else:
        result = "NO"
    return result
        
             

print(twoStrings("hello", "wrdlo"))