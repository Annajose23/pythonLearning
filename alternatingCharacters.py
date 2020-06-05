def alternatingCharacters(s):
    count = 0
    string_len = len(set(s))
    if string_len == 1:
        return len(s)-1
    else:
        for index,item in enumerate(s[:-1]):
            if item != s[index + 1]:
                pass
            else:
                count += 1
    return count





alternatingCharacters("AAAAA")