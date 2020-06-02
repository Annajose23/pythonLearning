def sherlockAndAnagrams(s):
    n = len(s)
    res = 0
    for i in range(1,n):
        dict = {}
        for j in range(n-i+1):
            substring = ''.join(sorted(s[j:j+i]))
            if substring in dict:
                dict[substring] += 1
            else:
                dict[substring] = 1
            res += dict[substring]-1
    return res

sherlockAndAnagrams("cdcd")
