from collections import Counter

def makeAnagram(a,b):
    arr1 = list((Counter(a) - Counter(b)).elements())
    arr2 = list((Counter(b) - Counter(a)).elements())
    return len(arr1 + arr2)




print(makeAnagram("cde","dcf"))